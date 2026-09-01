# -*- coding: utf-8 -*-
"""
替换 3 部 AI 兜底封面为真公版书影：穆天子传 / 神异经 / 新中国

难点：CADAL 合订 djvu 的 page 1 往往是函套/扉页——空白。
对策：抓取多个候选文件的多个页面，用「内容密度」自动筛出真正有字的内页：
      灰度标准差 × 暗像素比例，越高说明字越多（空白页接近 0）。

出网规则：
  Commons 走代理（127.0.0.1:7892）
  书格走直连
"""
import io
import json
import os
import sys
import time
import urllib.parse
import urllib.request

PROXY = "http://127.0.0.1:7892"
UA = {"User-Agent": "chinese-sf-covers/1.0 (educational project)"}

TARGETS = {
    "mutianzizhuan": {
        "title": "穆天子传",
        "queries": [
            "穆天子傳",
            "穆天子传",
            "Mu tianzi zhuan",
        ],
    },
    "shenyijing": {
        "title": "神异经",
        "queries": [
            "神異經",
            "神异经",
            "Shen yi jing",
        ],
    },
    "xinzhongguo-lu": {
        "title": "新中国",
        "queries": [
            "新中國 陸士諤",
            "新中国 陆士谔",
            "繪圖新中國",
        ],
    },
}

MAX_PAGES = 8


def make_opener(use_proxy: bool):
    if use_proxy:
        return urllib.request.build_opener(
            urllib.request.ProxyHandler({"http": PROXY, "https": PROXY})
        )
    return urllib.request.build_opener(urllib.request.ProxyHandler({}))


def fetch(url: str, opener, timeout: int = 40) -> bytes | None:
    try:
        req = urllib.request.Request(url, headers=UA)
        with opener.open(req, timeout=timeout) as r:
            return r.read()
    except Exception as e:
        print(f"      ! {type(e).__name__}: {str(e)[:70]}")
        return None


def commons_search(query: str, opener, rows: int = 8) -> list[str]:
    """返回候选 File 标题列表"""
    url = (
        "https://commons.wikimedia.org/w/api.php?action=query&format=json"
        f"&list=search&srsearch={urllib.parse.quote(query)}"
        f"&srnamespace=6&srlimit={rows}"
    )
    data = fetch(url, opener)
    if not data:
        return []
    try:
        js = json.loads(data.decode("utf-8"))
        return [h["title"] for h in js.get("query", {}).get("search", [])]
    except Exception:
        return []


def commons_page(title: str, page: int, width: int, opener) -> bytes | None:
    """取 File 的指定页渲染图"""
    fn = urllib.parse.quote(title.replace("File:", ""))
    url = f"https://commons.wikimedia.org/wiki/Special:FilePath/{fn}?page={page}&width={width}"
    return fetch(url, opener, timeout=60)


def content_score(data: bytes) -> float:
    """
    内容密度：越高越像"有字的页面"。
    用 PIL 转灰度 → 标准差（对比度） × 暗像素比例（墨迹占比）
    """
    try:
        from PIL import Image
    except ImportError:
        return 0.0
    try:
        im = Image.open(io.BytesIO(data)).convert("L")
        im.thumbnail((300, 420))
        px = list(im.getdata())
        n = len(px)
        if n == 0:
            return 0.0
        mean = sum(px) / n
        var = sum((p - mean) ** 2 for p in px) / n
        std = var ** 0.5
        dark = sum(1 for p in px if p < 140) / n
        # 太黑（全墨）或太白（空白）都降权
        penalty = 1.0 if 0.02 < dark < 0.75 else 0.15
        return std * min(dark, 0.5) * 4 * penalty
    except Exception:
        return 0.0


def main():
    op_proxy = make_opener(True)
    only = sys.argv[1] if len(sys.argv) > 1 else None

    os.makedirs("tmp_pd", exist_ok=True)
    report = {}

    for slug, cfg in TARGETS.items():
        if only and slug != only:
            continue
        print(f"\n===== {slug} 《{cfg['title']}》 =====")
        best = {"score": 0.0, "data": None, "src": None, "page": None}

        for q in cfg["queries"]:
            if best["score"] > 30:  # 已找到很好的，不再继续
                break
            print(f"  [搜索] {q}")
            hits = commons_search(q, op_proxy)
            print(f"    候选 {len(hits)} 个")
            for h in hits:
                if best["score"] > 30:
                    break
                print(f"    - {h[:60]}")
                for p in range(1, MAX_PAGES + 1):
                    data = commons_page(h, p, 900, op_proxy)
                    if not data or len(data) < 8000:
                        break  # 该文件没有这么多页
                    sc = content_score(data)
                    if sc > best["score"]:
                        best = {
                            "score": sc,
                            "data": data,
                            "src": h,
                            "page": p,
                        }
                        print(f"      p{p} score={sc:.1f} ↑ 新最佳")
                    time.sleep(0.8)
                time.sleep(1.0)

        if best["data"] and best["score"] > 6:
            out = f"public/covers/{slug}-pd.jpg"
            open(out, "wb").write(best["data"])
            size = os.path.getsize(out)
            print(
                f"  ✓ 保存 {out} ({size//1024} KB)  score={best['score']:.1f}\n"
                f"    来源 {best['src']} page={best['page']}"
            )
            report[slug] = {
                "ok": True,
                "file": f"{slug}-pd.jpg",
                "score": round(best["score"], 1),
                "source": best["src"],
                "page": best["page"],
                "sourceUrl": "https://commons.wikimedia.org/wiki/"
                + urllib.parse.quote(best["src"].replace(" ", "_")),
            }
            # 预览缩略图供人工核对
            try:
                from PIL import Image

                im = Image.open(out)
                im.thumbnail((300, 420))
                im.save(f"tmp_pd/{slug}_preview.jpg", quality=82)
            except Exception:
                pass
        else:
            print(f"  ✗ 未找到可用公版图（最佳 score={best['score']:.1f}）")
            report[slug] = {"ok": False, "score": round(best["score"], 1)}

    json.dump(report, open("tmp_pd/report.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    print("\n报告已写入 tmp_pd/report.json")


if __name__ == "__main__":
    main()
