#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
为公版古籍/晚清作品补齐真实封面图（PD book scans）。
来源优先级：Wikimedia Commons（PD/CC 书影） -> archive.org（扫描本扉页）。
内置限速（>=3s/次）与 429 退避（75s，最多重试 3 次），避免再次被封。
仅处理 frontmatter 中 coverCredit=public-domain 且尚未接 cover 的作品。
"""
import os, re, json, time, sys, urllib.request, urllib.parse, ssl

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COVERS = os.path.join(ROOT, "public", "covers")
ZH = os.path.join(ROOT, "src", "content", "works", "zh")
EN = os.path.join(ROOT, "src", "content", "works", "en")
UA = "chinese-sf-archive-bot/1.0 (educational; contact: admin@local)"
CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

# (slug, 检索词)
TARGETS = [
    ("bowuzhi", "博物志 张华"),
    ("mutianzizhuan", "穆天子传"),
    ("shenyijing", "神异经"),
    ("shiyiji", "拾遗记 王嘉"),
    ("shizhouji", "十洲记"),
    ("soushenji", "搜神记 干宝"),
    ("jinghuayuan", "镜花缘 李汝珍"),
    ("taipingguangji", "太平广记"),
    ("xinfaluo", "新法螺先生谭"),
    ("xinshitouji", "新石头记 吴趼人"),
    ("xinzhongguo-lu", "新中国 梁启超"),
    ("xinzhongguo-weilaiji", "新中国未来记 梁启超"),
    ("yuejie-lvxing", "月界旅行 凡尔纳"),
    ("yueqiu", "月球殖民地小说"),
]

PACE = 3.0
BACKOFF = 75
MAX_RETRY = 3

def get(url, timeout=40):
    last = None
    for attempt in range(MAX_RETRY):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
                return r.read(), r.headers.get("Content-Type", "")
        except urllib.error.HTTPError as e:
            if e.code == 429:
                last = f"429 @ {url}"
                print(f"  [429] 退避 {BACKOFF}s ...", flush=True)
                time.sleep(BACKOFF)
                continue
            last = f"HTTP {e.code} @ {url}"
            raise
    raise RuntimeError(f"retry exhausted: {last}")

def pause():
    time.sleep(PACE)

def wikimedia_image(query):
    q = urllib.parse.quote(query)
    api = (f"https://commons.wikimedia.org/w/api.php?action=query&generator=search"
           f"&gsrsearch={q}&gsrnamespace=6&gsrlimit=6&prop=imageinfo"
           f"&iiprop=url%7Cmime%7Cextmetadata&iiurlwidth=1200&format=json")
    raw, _ = get(api); pause()
    data = json.loads(raw)
    pages = (data.get("query", {}).get("pages", {}) or {}).values()
    for pg in pages:
        ii = pg.get("imageinfo", [{}])[0]
        mime = ii.get("mime", "")
        if not mime.startswith("image"):
            continue
        em = ii.get("extmetadata", {})
        lic = (em.get("LicenseShortName", {}).get("value", "") or "").lower()
        if not ("public domain" in lic or lic.startswith("cc") or "cc0" in lic):
            continue
        # prefer a tall book-scan thumb
        url = ii.get("thumburl") or ii.get("url")
        return url, ii.get("descriptionurl", "")
    return None, None

def archive_identifier(query):
    q = urllib.parse.quote(f"title:({query}) AND mediatype:texts")
    api = (f"https://archive.org/advancedsearch.php?q={q}"
           f"&fl[]=identifier&rows=5&output=json")
    raw, _ = get(api); pause()
    data = json.loads(raw)
    docs = data.get("response", {}).get("docs", [])
    for d in docs:
        ident = d.get("identifier")
        if ident:
            return ident
    return None

def archive_page_image(ident):
    # try title page n1, then cover n0
    for n in (1, 0, 2):
        url = f"https://archive.org/download/{ident}/page/n{n}_w1200.jpg"
        try:
            raw, ct = get(url)
            if raw and len(raw) > 20000 and ct.startswith("image"):
                return raw, url
        except Exception as e:
            print(f"    archive page n{n} failed: {e}", flush=True)
        pause()
    return None, None

def download_bytes(url):
    raw, ct = get(url)
    if raw and len(raw) > 20000 and ct.startswith("image"):
        return raw, ct
    return None, ct

def wire(slug, relpath, source):
    for d in (ZH, EN):
        p = os.path.join(d, slug + ".md")
        if not os.path.exists(p):
            continue
        lines = open(p, encoding="utf-8").read().splitlines()
        out, saw_credit, saw_cover = [], False, False
        for ln in lines:
            if ln.startswith("coverCredit:"):
                saw_credit = True
                out.append(ln)
                # insert cover + coverSource after credit
                out.append(f'cover: "{relpath}"')
                out.append(f'coverSource: "{source}"')
                continue
            if ln.startswith("cover:"):
                saw_cover = True
            out.append(ln)
        if not saw_credit:  # fallback: append before closing ---
            out2 = []
            for ln in out:
                if ln.strip() == "---" and not saw_cover:
                    out2.append(f'cover: "{relpath}"')
                    out2.append(f'coverSource: "{source}"')
                out2.append(ln)
            out = out2
        open(p, "w", encoding="utf-8").write("\n".join(out) + "\n")

def already_wired(slug):
    p = os.path.join(ZH, slug + ".md")
    if not os.path.exists(p):
        return False
    return bool(re.search(r'^cover:\s*"/covers/', open(p, encoding="utf-8").read(), re.M))

def main():
    os.makedirs(COVERS, exist_ok=True)
    report = []
    for slug, query in TARGETS:
        if already_wired(slug):
            print(f"[skip] {slug} 已接线", flush=True)
            continue
        print(f"\n=== {slug} ({query}) ===", flush=True)
        url, src = None, None
        # 1) Wikimedia
        try:
            wurl, wsrc = wikimedia_image(query)
            if wurl:
                b, ct = download_bytes(wurl)
                if b:
                    url, src = wurl, wsrc or wurl
                    open(os.path.join(COVERS, slug + ".jpg"), "wb").write(b)
                    print(f"  Wikimedia OK ({len(b)}B)", flush=True)
        except Exception as e:
            print(f"  Wikimedia err: {e}", flush=True)
        # 2) archive.org fallback
        if not url:
            try:
                ident = archive_identifier(query)
                if ident:
                    print(f"  archive id={ident}", flush=True)
                    b, aurl = archive_page_image(ident)
                    if b:
                        url, src = aurl, f"https://archive.org/details/{ident}"
                        open(os.path.join(COVERS, slug + ".jpg"), "wb").write(b)
                        print(f"  archive OK ({len(b)}B)", flush=True)
            except Exception as e:
                print(f"  archive err: {e}", flush=True)
        if url:
            wire(slug, f"/covers/{slug}.jpg", src)
            print(f"  -> wired {slug}.jpg", flush=True)
            report.append({"slug": slug, "status": "ok", "source": src})
        else:
            print(f"  !! no image found", flush=True)
            report.append({"slug": slug, "status": "no_image"})
    json.dump(report, open(os.path.join(ROOT, "scripts", "pd_remaining_report.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    print("\nDONE. report -> scripts/pd_remaining_report.json", flush=True)

if __name__ == "__main__":
    main()
