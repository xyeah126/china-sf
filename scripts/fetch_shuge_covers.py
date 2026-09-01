#!/usr/bin/env python3
# 从「书格」(shuge.org，国内公有领域古籍数字化站) 采集古籍书影
#
# 两个关键点（踩坑总结）：
#   1. 书格必须【直连】，走环境代理会 403/000 → 用 ProxyHandler({}) 绕开代理
#   2. 条目页有 JS 跳转 + Cookie 反爬：首次请求返 403（内含种 cookie 的 JS），
#      带上 cookie 再请求才返回 200 → 用 CookieJar + 两次请求
#
# 图片命名规律：<slug><NN>-<W>x<H>.jpg，NN=01 即封面首页。
import http.cookiejar
import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "public" / "covers"
BASE = "https://www.shuge.org"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

# slug -> 检索用书名
TARGETS = {
    "mutianzizhuan": "穆天子传",
    "shenyijing": "神异经",
    "shiyiji": "拾遗记",
    "shizhouji": "十洲记",
    "bowuzhi": "博物志",
    "soushenji": "搜神记",
    "youyangzazu": "酉阳杂俎",
    "taipingguangji": "太平广记",
    "jinghuayuan": "镜花缘",
    "xinzhongguo-weilaiji": "新中国未来记",
    "yuejie-lvxing": "月界旅行",
    "xinshitouji": "新石头记",
    "xinfaluo": "新法螺",
}

# 站点 UI 资源，不是书影，需排除
UI_NOISE = ("banian", "9nian", "mpshuge", "shiweijianji", "logo", "shugeorg")

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(
    urllib.request.ProxyHandler({}),          # 关键：绕开代理，直连
    urllib.request.HTTPCookieProcessor(cj),
)
opener.addheaders = [
    ("User-Agent", UA),
    ("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"),
    ("Accept-Language", "zh-CN,zh;q=0.9"),
    ("Referer", BASE + "/"),
]


def fetch(url, tries=2):
    """首次请求可能 403（含种 cookie 的 JS），带 cookie 重试即可拿到 200。"""
    last = None
    for _ in range(tries + 1):
        try:
            with opener.open(url, timeout=25) as r:
                return r.read().decode("utf-8", "ignore")
        except Exception as e:  # noqa: BLE001
            last = e
            time.sleep(1.5)
    print(f"    ! 抓取失败: {last}")
    return ""


def norm(s):
    return re.sub(r"[\s《》〈〉·、，,。\.\[\]]", "", s).strip()


def search_entries(book):
    """站内搜索，返回 [(title, url, slug)]"""
    url = BASE + "/?s=" + urllib.parse.quote(book)
    html = fetch(url)
    if not html:
        return []
    pat = re.compile(
        r"<h2[^>]*portfolio-grid-title[^>]*>.*?<a href='([^']+/view/([^/]+)/)'>(.*?)</a>",
        re.S)
    out = []
    for m in pat.finditer(html):
        link, slug, title = m.group(1), m.group(2), m.group(3)
        title = re.sub(r"<[^>]+>", "", title).strip()
        out.append((title, link, slug))
    # 同 slug 去重
    seen, uniq = set(), []
    for it in out:
        if it[2] not in seen:
            seen.add(it[2])
            uniq.append(it)
    return uniq


def pick_entry(entries, book):
    """优先书名完全一致，其次以书名开头，最后包含书名。"""
    nb = norm(book)
    exact = [e for e in entries if norm(e[0]) == nb]
    if exact:
        return exact[0], "exact"
    starts = [e for e in entries if norm(e[0]).startswith(nb)]
    if starts:
        return starts[0], "startswith"
    contains = [e for e in entries if nb in norm(e[0])]
    if contains:
        return contains[0], "contains"
    return None, ""


def pick_image(html, slug):
    """取该书的首页书影：<slug>01-... 优先，否则取主内容区第一张大图。"""
    all_imgs = re.findall(
        r"https://www\.shuge\.org/wp-content/uploads/\d{4}/\d{2}/"
        r"[A-Za-z0-9_.\-]+\.(?:jpg|jpeg|png)", html)
    # 去重保序
    seen, imgs = set(), []
    for u in all_imgs:
        if u not in seen:
            seen.add(u)
            imgs.append(u)

    def clean(u):
        name = u.rsplit("/", 1)[-1].lower()
        return not any(n in name for n in UI_NOISE)

    cand = [u for u in imgs if clean(u)]
    # 1) 与 slug 同名前缀，且编号 01
    pref = re.compile(rf"/{re.escape(slug)}0*1-\d+x\d+\.(jpg|jpeg|png)$", re.I)
    for u in cand:
        if pref.search(u):
            return u
    # 2) 与 slug 同名前缀的任意一张（取编号最小）
    pref2 = re.compile(rf"/{re.escape(slug)}(\d+)-\d+x\d+\.(jpg|jpeg|png)$", re.I)
    numbered = []
    for u in cand:
        m = pref2.search(u)
        if m:
            numbered.append((int(m.group(1)), u))
    if numbered:
        return sorted(numbered)[0][1]
    # 3) 兜底：主内容区第一张（排除侧栏 710x375 缩略图）
    for u in cand:
        if "710x375" not in u:
            return u
    return cand[0] if cand else ""


def download(url, dest):
    try:
        with opener.open(url, timeout=60) as r:
            data = r.read()
        if len(data) < 4096:
            raise ValueError("too small")
        dest.write_bytes(data)
        return len(data)
    except Exception as e:  # noqa: BLE001
        print(f"    ! 下载失败: {e}")
        return 0


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    report = []

    for slug, book in TARGETS.items():
        print(f"\n=== {slug}  ({book}) ===", flush=True)
        entries = search_entries(book)
        if not entries:
            print("  搜索无结果", flush=True)
            report.append({"slug": slug, "status": "no_result"})
            time.sleep(1.5)
            continue
        chosen, how = pick_entry(entries, book)
        if not chosen:
            print(f"  {len(entries)} 条候选但书名不匹配，前3：", flush=True)
            for t, _, _ in entries[:3]:
                print(f"     - {t}", flush=True)
            report.append({"slug": slug, "status": "no_match",
                           "candidates": [t for t, _, _ in entries[:3]]})
            time.sleep(1.5)
            continue
        title, link, eslug = chosen
        print(f"  命中[{how}] {title}  ->  /view/{eslug}/", flush=True)

        html = fetch(link)
        if not html:
            report.append({"slug": slug, "status": "fetch_failed", "link": link})
            time.sleep(1.5)
            continue
        img = pick_image(html, eslug)
        if not img:
            print("  未找到书影图", flush=True)
            report.append({"slug": slug, "status": "no_image", "link": link})
            time.sleep(1.5)
            continue
        ext = ".jpg" if img.lower().endswith((".jpg", ".jpeg")) else ".png"
        dest = OUT_DIR / f"{slug}{ext}"
        n = download(img, dest)
        if not n:
            report.append({"slug": slug, "status": "download_failed", "link": link})
            time.sleep(1.5)
            continue
        print(f"  ✓ {dest.name}  {n // 1024} KB", flush=True)
        report.append({"slug": slug, "status": "ok", "file": dest.name,
                       "title": title, "page": link, "direct": img, "size": n})
        time.sleep(2)  # 礼貌间隔

    out = ROOT / "scripts" / "shuge_report.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print("\n\n===== 汇总 =====", flush=True)
    for r in report:
        if r["status"] == "ok":
            print(f"OK   {r['slug']:24s} {r['file']:28s} {r['title']}")
        else:
            print(f"--   {r['slug']:24s} {r['status']}")


if __name__ == "__main__":
    main()
