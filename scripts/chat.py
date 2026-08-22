#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
عميل بسيط لمحادثة النموذج العربي Qwen3-1.7B
يتصل بالخادم المحلي عبر API (OpenAI-compatible)

الاستخدام:
    1) شغّل الخادم أولًا:  bash scripts/run-server.sh
    2) نفّذ:              python3 scripts/chat.py
"""
import json
import urllib.request

BASE_URL = "http://localhost:8080/v1/chat/completions"


def ask(question: str, max_tokens: int = 256) -> str:
    payload = {
        "messages": [{"role": "user", "content": question}],
        "max_tokens": max_tokens,
        "temperature": 0.7,
    }
    req = urllib.request.Request(
        BASE_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    return data["choices"][0]["message"]["content"]


def main():
    print("=" * 50)
    print("🤖 مساعد Qwen3-1.7B العربي — اكتب سؤالك بالعربية")
    print("   (اكتب 'خروج' للإنهاء)")
    print("=" * 50)
    while True:
        try:
            q = input("\nأنت: ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not q or q in ("خروج", "exit", "quit"):
            break
        print("المساعد: ", end="", flush=True)
        try:
            print(ask(q))
        except Exception as e:
            print(f"(خطأ في الاتصال بالخادم: {e})")


if __name__ == "__main__":
    main()
