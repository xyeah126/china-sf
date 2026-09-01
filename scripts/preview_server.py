#!/usr/bin/env python3
"""本地预览服务器（禁用缓存版）

用途：预览 dist 目录时强制浏览器不使用缓存，避免封面/资源更新后
浏览器仍显示旧图（python -m http.server 不发 Cache-Control 头，
浏览器会按启发式规则缓存静态资源，导致改了图却看不到新图）。

用法：
    python scripts/preview_server.py [port] [dir]
默认：port=4550, dir=dist
"""
import functools
import http.server
import socketserver
import sys


class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    """在每个响应上加 no-store，强制每次重新拉取。"""

    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def log_message(self, fmt, *args):  # 减少噪音，只打路径
        sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 4550
    root = sys.argv[2] if len(sys.argv) > 2 else "dist"

    handler = functools.partial(NoCacheHandler, directory=root)
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.ThreadingTCPServer(("", port), handler) as httpd:
        print(f"Serving '{root}' on http://localhost:{port}  (cache disabled)")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nstopped")


if __name__ == "__main__":
    main()
