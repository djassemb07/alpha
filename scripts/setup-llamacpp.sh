#!/usr/bin/env bash
# ============================================================
# تنصيب llama.cpp (محرك تشغيل النماذج) - إصدار Linux x64
# ============================================================

set -e

VERSION="b10582"
URL="https://github.com/ggml-org/llama.cpp/releases/download/${VERSION}/llama-${VERSION}-bin-ubuntu-x64.tar.gz"
DEST="llama"

echo "📦 تنصيب llama.cpp ($VERSION)..."

if [ -x "$DEST/llama-server" ]; then
    echo "✅ llama.cpp مثبت بالفعل"
    exit 0
fi

echo "⏳ تحميل..."
curl -L --progress-bar -o llama.tar.gz "$URL"
mkdir -p "$DEST"
tar -xzf llama.tar.gz -C "$DEST" --strip-components=1
rm -f llama.tar.gz

# إضافة المسار
if ! grep -q "llama/bin" ~/.bashrc 2>/dev/null; then
    echo 'export PATH="$HOME/llama/bin:$PATH"' >> ~/.bashrc
    echo 'export LD_LIBRARY_PATH="$HOME/llama:$LD_LIBRARY_PATH"' >> ~/.bashrc
fi

echo "✅ تم التنصيب. أعد فتح الطرفية أو نفّذ: source ~/.bashrc"
