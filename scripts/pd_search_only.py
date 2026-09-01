#!/usr/bin/env python3
# 第一步：只检索不下载。输出候选标题 + mime/尺寸/大小 + 相关性标记，供人工挑选。
import json
import time
import urllib.parse
import urllib.request

API = "https://commons.wikimedia.org/w/api.php"
UA = "ChineseSF-Archive/1.0 (static educational archive; local build script)"

# 已完成的作品，跳过（避免重复请求触发限流）
DONE = {"shanhaijing", "huainanzi", "liezi-tangwen"}

# slug -> (检索词列表, 相关性关键词列表)
JOBS = {
    "shanhaijing": (["山海经", "Shan Hai Jing illustration"],
                    ["shan hai jing", "shanhaijing", "山海经", "山海經"]),
    "huainanzi": (["淮南子", "Huainanzi"],
                  ["huainanzi", "huai nan zi", "淮南子", "淮南鴻烈"]),
    "liezi-tangwen": (["列子", "Liezi"],
                      ["liezi", "lie zi", "列子"]),
    "mutianzizhuan": (["穆天子传", "Mu Tianzi Zhuan"],
                      ["mu tianzi", "mutianzi", "穆天子"]),
    "shenyijing": (["神异经", "Shenyi Jing"],
                   ["shenyi jing", "shenyijing", "神异经", "神異經"]),
    "shiyiji": (["拾遗记", "Shiyiji Wang Jia"],
                ["拾遗记", "拾遺記", "shiyiji", "shi yi ji"]),
    "shizhouji": (["十洲记", "Shizhouji"],
                  ["十洲", "shizhou", "shi zhou ji", "海內十洲"]),
    "bowuzhi": (["博物志", "Bowuzhi Zhang Hua"],
                ["博物志", "bowuzhi", "bo wu zhi"]),
    "soushenji": (["搜神记", "Soushenji Gan Bao"],
                  ["搜神", "soushen", "sou shen ji"]),
    "youyangzazu": (["酉阳杂俎", "Youyang Zazu"],
                    ["酉阳", "酉陽", "youyang", "you yang za zu"]),
    "taipingguangji": (["太平广记", "Taiping Guangji"],
                       ["太平广记", "太平廣記", "taiping guangji", "taiping"]),
    "xiyouji": (["西游记 插图", "Journey to the West illustration"],
                ["xiyouji", "xi you ji", "journey to the west", "西游记", "西遊記"]),
    "jinghuayuan": (["镜花缘", "Jinghuayuan Flowers in the Mirror"],
                    ["镜花缘", "鏡花緣", "jinghuayuan", "jing hua yuan", "flowers in the mirror"]),
    "xinzhongguo-weilaiji": (["新中国未来记", "Xin Zhongguo Weilai Ji"],
                             ["新中国未来记", "新中國未來記", "xin zhongguo", "weilai ji"]),
    "yuejie-lvxing": (["月界旅行", "Yuejie Luxing"],
                      ["月界旅行", "yuejie", "yue jie"]),
    "xinshitouji": (["新石头记", "Xin Shitou Ji"],
                    ["新石头记", "新石頭記", "xin shitou", "shi tou ji"]),
    "xinfaluo": (["新法螺", "Xin Faluo"],
                 ["新法螺", "xin faluo", "faluo"]),
}

OK_MIME = {"image/jpeg", "image/png", "image/webp"}
MIN_W, MIN_H = 700, 500
MAX_BYTES = 6 * 1024 * 1024


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
            time.sleep(1.0)
    print(f"    ! API 失败: {last}", flush=True)
    return {}


def main():
    for slug, (queries, keywords) in JOBS.items():
        if slug in DONE:
            continue
        print(f"\n=== {slug} ===", flush=True)
        titles = []
        for q in queries:
            d = api({"action": "query", "list": "search", "srsearch": q,
                     "srnamespace": 6, "srlimit": 10})
            got = [x["title"] for x in d.get("query", {}).get("search", [])]
            titles.extend(got)
            time.sleep(2.5)  # 限速：避免 429
        seen, uniq = set(), []
        for t in titles:
            if t not in seen:
                seen.add(t)
                uniq.append(t)

        d = api({"action": "query", "titles": "|".join(uniq[:28]),
                 "prop": "imageinfo", "iiprop": "url|extmetadata|mime|size"})
        kept = []
        for p in d.get("query", {}).get("pages", {}).values():
            ii = p.get("imageinfo")
            if not ii:
                continue
            info = ii[0]
            em = info.get("extmetadata", {})
            lic = (em.get("LicenseShortName", {}).get("value", "") or "").strip()
            blob = (lic + " " + (em.get("UsageTerms", {}).get("value", "") or "")).lower()
            pd = any(t in blob for t in ("public domain", "cc0", "pdm"))
            mime = info.get("mime", "")
            w, h = info.get("width", 0), info.get("height", 0)
            size = info.get("size", 0)
            title = p["title"]
            low = title.lower()
            rel = any(k in low for k in keywords)
            ok = (pd and mime in OK_MIME and w >= MIN_W and h >= MIN_H and size <= MAX_BYTES)
            if ok:
                kept.append((title, lic, w, h, size, rel, info.get("url")))
        kept.sort(key=lambda x: (not x[5], -x[2] * x[3]))
        if not kept:
            print("  (无满足条件的候选：PD + jpg/png/webp + ≥700x500 + ≤6MB)")
        for title, lic, w, h, size, rel, _ in kept[:6]:
            flag = "★相关" if rel else "  存疑"
            print(f"  {flag} [{w}x{h}] {size//1024:>6}KB  {lic:<18s} {title}")
        time.sleep(0.3)


if __name__ == "__main__":
    main()
