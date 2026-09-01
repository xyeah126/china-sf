#!/usr/bin/env python3
# 为古代 / 晚清作品从 Wikimedia Commons 采集公有领域配图
# SOP 8.5：公版优先。未通过 PD 许可校验的图一律不下载、不标注 public-domain。
import json
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "public" / "covers"
API = "https://commons.wikimedia.org/w/api.php"
UA = "ChineseSF-Archive/1.0 (static educational archive; local build script)"

# 作品 slug -> 检索词（中英文各一组，取并集）
QUERIES = {
    "shanhaijing": ["山海经", "Shan Hai Jing illustration"],
    "huainanzi": ["淮南子", "Huainanzi"],
    "liezi-tangwen": ["列子", "Liezi"],
    "mutianzizhuan": ["穆天子传", "Mu Tianzi Zhuan"],
    "shenyijing": ["神异经", "Shenyi Jing"],
    "shiyiji": ["拾遗记", "Shiyiji Wang Jia"],
    "shizhouji": ["十洲记", "Shizhouji"],
    "bowuzhi": ["博物志", "Bowuzhi Zhang Hua"],
    "soushenji": ["搜神记", "Soushenji Gan Bao"],
    "youyangzazu": ["酉阳杂俎", "Youyang Zazu"],
    "taipingguangji": ["太平广记", "Taiping Guangji"],
    "xiyouji": ["西游记 插图", "Journey to the West illustration"],
    "jinghuayuan": ["镜花缘", "Jinghuayuan Flowers in the Mirror"],
    "xinzhongguo-weilaiji": ["新中国未来记", "Xin Zhongguo Weilai Ji"],
    "yuejie-lvxing": ["月界旅行", "Yuejie Luxing"],
    "xinshitouji": ["新石头记", "Xin Shitou Ji"],
    "xinfaluo": ["新法螺", "Xin Faluo"],
}

PD_TOKENS = ("public domain", "cc0", "pdm", "no restrictions")


def api(params, tries=2):
    params = dict(params)
    params["format"] = "json"
    url = API + "?" + urllib.parse.urlencode(params)
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=12) as r:
                return json.load(r)
        except Exception as e:  # noqa: BLE001
            last = e
            print(f"    ! API 重试{i+1}: {type(e).__name__}", flush=True)
            time.sleep(1.0)
    print(f"    ! API 失败: {last}", flush=True)
    return {}


def search(q, limit=12):
    d = api({"action": "query", "list": "search", "srsearch": q,
             "srnamespace": 6, "srlimit": limit})
    return [x["title"] for x in d.get("query", {}).get("search", [])]


def imageinfo(titles):
    if not titles:
        return {}
    d = api({"action": "query", "titles": "|".join(titles),
             "prop": "imageinfo", "iiprop": "url|extmetadata|mime|size"})
    out = {}
    for p in d.get("query", {}).get("pages", {}).values():
        ii = p.get("imageinfo")
        if not ii:
            continue
        info = ii[0]
        em = info.get("extmetadata", {})
        out[p["title"]] = {
            "url": info.get("url"),
            "mime": info.get("mime"),
            "width": info.get("width"),
            "height": info.get("height"),
            "license": (em.get("LicenseShortName", {}).get("value", "") or "").strip(),
            "usage": (em.get("UsageTerms", {}).get("value", "") or "").strip(),
            "page": "https://commons.wikimedia.org/wiki/"
                    + urllib.parse.quote(p["title"].replace(" ", "_")),
        }
    return out


def is_pd(rec):
    blob = (rec.get("license", "") + " " + rec.get("usage", "")).lower()
    return any(t in blob for t in PD_TOKENS)


def ext_for(mime):
    return {
        "image/jpeg": ".jpg",
        "image/png": ".png",
        "image/webp": ".webp",
        "image/gif": ".gif",
        "image/tiff": ".tif",
    }.get((mime or "").lower(), ".jpg")


def download(url, dest, tries=2):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=25) as r:
                data = r.read()
            if len(data) < 1024:
                raise ValueError("file too small")
            dest.write_bytes(data)
            return len(data)
        except Exception as e:  # noqa: BLE001
            last = e
            print(f"    ! 下载重试{i+1}: {type(e).__name__}", flush=True)
            time.sleep(1.0)
    print(f"    ! 下载失败: {last}", flush=True)
    return 0


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    report = []

    for slug, queries in QUERIES.items():
        print(f"\n=== {slug} ===", flush=True)
        titles = []
        for q in queries:
            got = search(q)
            print(f"  检索「{q}」-> {len(got)} 条", flush=True)
            titles.extend(got)
            time.sleep(0.3)
        # 去重保序
        seen, uniq = set(), []
        for t in titles:
            if t not in seen:
                seen.add(t)
                uniq.append(t)

        recs = imageinfo(uniq[:24])
        # 只保留 PD，且是位图
        pd_recs = [(t, r) for t, r in recs.items()
                   if is_pd(r) and (r.get("mime") or "").startswith("image")
                   and not (r.get("mime") or "").endswith("svg")]
        if not pd_recs:
            print("  -> 无可用的 PD 图片（跳过）")
            report.append({"slug": slug, "status": "none"})
            continue

        # 偏好：文件名含 illustration/woodcut/图/刻 的古籍插图
        def score(item):
            t = item[0].lower()
            s = 0
            for kw in ("illustration", "woodcut", "图", "刻", "edition", "1800", "1700", "1600", "1500", "1400"):
                if kw in t:
                    s += 1
            if "cover" in t or "poster" in t:
                s -= 2  # 现代出版物封面/海报通常受版权保护
            return -s

        pd_recs.sort(key=score)
        # 保持 pd_recs 是 list
        chosen = None
        for title, rec in sorted(pd_recs, key=score):
            chosen = (title, rec)
            break
        title, rec = chosen
        ext = ext_for(rec["mime"])
        dest = OUT_DIR / f"{slug}{ext}"
        size = download(rec["url"], dest)
        if not size:
            report.append({"slug": slug, "status": "download_failed", "title": title})
            continue
        print(f"  -> 采用 {title}")
        print(f"     许可: {rec['license']} | {rec['width']}x{rec['height']} | {size//1024} KB")
        report.append({
            "slug": slug,
            "status": "ok",
            "file": dest.name,
            "title": title,
            "license": rec["license"],
            "page": rec["page"],
            "direct": rec["url"],
            "size": size,
        })
        time.sleep(0.5)

    (ROOT / "scripts" / "pd_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print("\n\n===== 汇总 =====")
    for r in report:
        if r["status"] == "ok":
            print(f"OK   {r['slug']:24s} {r['file']:28s} {r['license']}")
        else:
            print(f"--   {r['slug']:24s} {r['status']}")


if __name__ == "__main__":
    main()
