#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""针对主脚本 4 部 no_image 的作品做二次补齐。
Wikimedia 用多个检索词变体；archive.org 改用 services/img 封面 + 多种 page 图兜底。
限速 3s/次，429 退避 75s 重试 3 次。
"""
import os, re, json, time, ssl, urllib.request, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COVERS = os.path.join(ROOT, "public", "covers")
ZH = os.path.join(ROOT, "src", "content", "works", "zh")
EN = os.path.join(ROOT, "src", "content", "works", "en")
UA = "chinese-sf-archive-bot/1.0 (educational; contact: admin@local)"
CTX = ssl.create_default_context(); CTX.check_hostname = False; CTX.verify_mode = ssl.CERT_NONE
PACE, BACKOFF, MAX_RETRY = 3.0, 75, 3

FAILED = [
    ("mutianzizhuan", ["穆天子传", "穆天子傳", "穆天子传 汲冢书"]),
    ("taipingguangji", ["太平广记", "太平廣記", "太平广记 李昉"]),
    ("xinshitouji",   ["新石头记", "新石頭記", "新石头记 吴趼人"]),
    ("yueqiu",        ["月球殖民地小说", "月球殖民地小說", "月球殖民地"]),
]

def get(url, timeout=40):
    last = None
    for _ in range(MAX_RETRY):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
                return r.read(), r.headers.get("Content-Type", "")
        except urllib.error.HTTPError as e:
            if e.code == 429:
                print(f"  [429] 退避 {BACKOFF}s", flush=True); time.sleep(BACKOFF); continue
            raise
    raise RuntimeError(f"retry exhausted: {last}")

def pause(): time.sleep(PACE)

def wikimedia_image(queries):
    for q in queries:
        api = ("https://commons.wikimedia.org/w/api.php?action=query&generator=search"
               f"&gsrsearch={urllib.parse.quote(q)}&gsrnamespace=6&gsrlimit=6&prop=imageinfo"
               "&iiprop=url%7Cmime%7Cextmetadata&iiurlwidth=1200&format=json")
        try:
            raw, _ = get(api); pause()
        except Exception as e:
            print(f"    wm '{q}' err {e}", flush=True); continue
        data = json.loads(raw)
        for pg in (data.get("query", {}).get("pages", {}) or {}).values():
            ii = pg.get("imageinfo", [{}])[0]
            if not ii.get("mime", "").startswith("image"): continue
            em = ii.get("extmetadata", {})
            lic = (em.get("LicenseShortName", {}).get("value", "") or "").lower()
            if not ("public domain" in lic or lic.startswith("cc") or "cc0" in lic): continue
            url = ii.get("thumburl") or ii.get("url")
            return url, ii.get("descriptionurl", "")
    return None, None

def archive_image(query):
    q = urllib.parse.quote(f"title:({query}) AND mediatype:texts")
    api = f"https://archive.org/advancedsearch.php?q={q}&fl[]=identifier&rows=5&output=json"
    raw, _ = get(api); pause()
    ids = [d.get("identifier") for d in json.loads(raw).get("response", {}).get("docs", []) if d.get("identifier")]
    for ident in ids:
        for pat in (f"https://archive.org/services/img/{ident}",
                    f"https://archive.org/download/{ident}/{ident}_page_cover.jpg",
                    f"https://archive.org/download/{ident}/page/n1_w1200.jpg",
                    f"https://archive.org/download/{ident}/page/n0_w1200.jpg"):
            try:
                b, ct = get(pat); pause()
                if b and len(b) > 20000 and ct.startswith("image"):
                    return b, f"https://archive.org/details/{ident}"
            except Exception as e:
                print(f"    archive {pat} err {e}", flush=True)
    return None, None

def wire(slug, source):
    for d in (ZH, EN):
        p = os.path.join(d, slug + ".md")
        if not os.path.exists(p): continue
        lines = open(p, encoding="utf-8").read().splitlines(); out = []
        for ln in lines:
            if ln.startswith("coverCredit:"):
                out.append(ln); out.append(f'cover: "/covers/{slug}.jpg"'); out.append(f'coverSource: "{source}"'); continue
            out.append(ln)
        open(p, "w", encoding="utf-8").write("\n".join(out) + "\n")

def main():
    os.makedirs(COVERS, exist_ok=True); report = []
    for slug, queries in FAILED:
        print(f"\n=== retry {slug} ===", flush=True)
        url, src = wikimedia_image(queries)
        if not url:
            b, src = archive_image(queries[0])
            if b:
                open(os.path.join(COVERS, slug + ".jpg"), "wb").write(b); url = "archive"
        if url:
            if url != "archive":  # wikimedia path needs download
                b, ct = get(url)
                if b and len(b) > 20000:
                    open(os.path.join(COVERS, slug + ".jpg"), "wb").write(b)
                else:
                    url = None
            if url:
                wire(slug, src); print(f"  -> wired {slug}.jpg  ({src})", flush=True)
                report.append({"slug": slug, "status": "ok", "source": src}); continue
        print(f"  !! still no image", flush=True)
        report.append({"slug": slug, "status": "no_image"})
    json.dump(report, open(os.path.join(ROOT, "scripts", "pd_retry_report.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("\nRETRY DONE -> scripts/pd_retry_report.json", flush=True)

if __name__ == "__main__":
    main()
