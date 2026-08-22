#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
واجهة محادثة عربية على الويب لنموذج Qwen3-1.7B
يقدّم صفحة المحادثة ويوصل طلبات API إلى خادم llama-server

الاستخدام:
    1) شغّل خادم النموذج أولًا:  bash scripts/run-server.sh   (منفذ 8080)
    2) شغّل هذه الواجهة:        python3 scripts/web_chat.py  (منفذ 3000)
    3) افتح:                    http://localhost:3000
"""
import json
import urllib.request
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

WEB_DIR = Path(__file__).resolve().parent.parent / "web"
LLAMA_PORT = 8080
WEB_PORT = 3000


class ChatHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(WEB_DIR), **kwargs)

    def do_POST(self):
        if self.path == "/v1/chat/completions":
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length)

            # تمرير الطلب إلى خادم النموذج
            req = urllib.request.Request(
                f"http://localhost:{LLAMA_PORT}/v1/chat/completions",
                data=body,
                headers={"Content-Type": "application/json"},
            )
            try:
                with urllib.request.urlopen(req, timeout=180) as resp:
                    data = resp.read()
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(data)))
                self.end_headers()
                self.wfile.write(data)
            except Exception as e:
                err = json.dumps({"error": str(e)}).encode()
                self.send_response(500)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(err)))
                self.end_headers()
                self.wfile.write(err)
        else:
            self.send_error(404)

    def log_message(self, fmt, *args):
        pass  # إسكات السجلات


if __name__ == "__main__":
    print(f"🚀 واجهة المحادثة على http://localhost:{WEB_PORT}")
    print(f"   (تتصل بخادم النموذج على المنفذ {LLAMA_PORT})")
    HTTPServer(("0.0.0.0", WEB_PORT), ChatHandler).serve_forever()
