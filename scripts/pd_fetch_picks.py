#!/usr/bin/env python3
# 按人工确认的 Commons 文件标题，下载公有领域配图并写入 frontmatter 所需的 coverSource
import json
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "public" / "covers"
API = "https://commons.wikimedia.org/w/api.php"
UA = "ChineseSF-Archive/1.0 (static educational archive; local build script)"

# slug -> 人工挑选的 Commons 文件标题
# 说明：前三部（shanhaijing/huainanzi/liezi-tangwen）已下载，此处不再重复
PICKS = {
    # 1592 年金陵世德堂刊本《西游记》书影（公有领域）
    "xiyouji": "File:The Journey to the West, Shidetang Hall of Jinling in 1592.jpg",
}

PD_TOKENS = ("public domain", "cc0", "pdm")
OK_MIME = {"image/jpeg": ".jpg", "image/png": ".png", "image/webp": ".webp"}
MAX_BYTES = 8 * 1024 * 1024


def api(params, tries=2, timeout=12):
    params = dict(params)
    params["format"] = "json"
    url = API + "?" + urllib.parse.urlencode(params)
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return json.load(r)
        except Exception as e:  # noqa: BLE001
            last = e
            wait = 2 * (i + 1)
            print(f"    ! 重试{i+1} ({type(e).__name__}) 等待 {wait}s", flush=True)
            time.sleep(wait)
    print(f"    ! API 失败: {last}", flush=True)
    return {}


def download(url, dest, tries=3):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=30) as r:
                data = r.read()
            if len(data) < 2048:
                raise ValueError("file too small")
            dest.write_bytes(data)
            return len(data)
        except Exception as e:  # noqa: BLE001
            last = e
            time.sleep(2 * (i + 1))
    print(f"    ! 下载失败: {last}", flush=True)
    return 0


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    manifest = {}
    for slug, title in PICKS.items():
        print(f"\n=== {slug} ===", flush=True)
        d = api({"action": "query", "titles": title, "prop": "imageinfo",
                 "iiprop": "url|extmetadata|mime|size"})
        pages = d.get("query", {}).get("pages", {})
        rec = None
        for p in pages.values():
            if p.get("imageinfo"):
                rec = (p["title"], p["imageinfo"][0])
                break
        if not rec:
            print("  ! 未取到 imageinfo", flush=True)
            continue
        t, info = rec
        em = info.get("extmetadata", {})
        lic = (em.get("LicenseShortName", {}).get("value", "") or "").strip()
        blob = (lic + " " + (em.get("UsageTerms", {}).get("value", "") or "")).lower()
        if not any(tok in blob for tok in PD_TOKENS):
            print(f"  ! 许可证非公版，拒绝: {lic}", flush=True)
            continue
        mime = (info.get("mime") or "").lower()
        if mime not in OK_MIME:
            print(f"  ! 不支持的格式: {mime}", flush=True)
            continue
        if info.get("size", 0) > MAX_BYTES:
            print(f"  ! 文件过大: {info.get('size')}", flush=True)
            continue
        ext = OK_MIME[mime]
        dest = OUT_DIR / f"{slug}{ext}"
        n = download(info["url"], dest)
        if not n:
            continue
        page_url = "https://commons.wikimedia.org/wiki/" + urllib.parse.quote(
            t.replace(" ", "_"))
        manifest[slug] = {
            "file": dest.name,
            "commons_file": t,
            "page": page_url,
            "license": lic,
            "size": n,
            "width": info.get("width"),
            "height": info.get("height"),
        }
        print(f"  ✓ {dest.name}  {info.get('width')}x{info.get('height')}  {n//1024}KB  {lic}",
              flush=True)
        time.sleep(2)

    out = ROOT / "scripts" / "pd_manifest.json"
    # 与已有 manifest 合并，避免覆盖先前下载的记录
    if out.exists():
        try:
            manifest = {**json.loads(out.read_text(encoding="utf-8")), **manifest}
        except Exception:  # noqa: BLE001
            pass
    out.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nmanifest -> {out}（累计 {len(manifest)} 条）", flush=True)


if __name__ == "__main__":
    main()
