#!/usr/bin/env bash
# ============================================================
# تشغيل خادم Qwen3-1.7B العربي محليًا
# الاستخدام: bash scripts/run-server.sh
# ثم افتح: http://localhost:8080
# ============================================================

set -e

MODEL_FILE="model/Qwen3-1.7B-Q4_K_M.gguf"
PORT="${1:-8080}"

# 1) التأكد من وجود النموذج
if [ ! -f "$MODEL_FILE" ]; then
    echo "⚠️ النموذج غير موجود. جاري تحميله أولًا..."
    bash scripts/download-model.sh
fi

# 2) التأكد من وجود llama.cpp
if ! command -v llama-server &>/dev/null; then
    echo "⚠️ llama.cpp غير مثبت. جاري تحميله..."
    bash scripts/setup-llamacpp.sh
fi

echo "🚀 تشغيل الخادم على http://localhost:$PORT"
echo "   (اضغط Ctrl+C للإيقاف)"

export LD_LIBRARY_PATH="$(dirname $(command -v llama-server)):$LD_LIBRARY_PATH"
llama-server -m "$MODEL_FILE" --host 0.0.0.0 --port "$PORT" --ctx-size 4096 --threads 4
