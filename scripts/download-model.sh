#!/usr/bin/env bash
# ============================================================
# تحميل نموذج Qwen3-1.7B (GGUF Q4_K_M) من Hugging Face
# الحجم: ~1.1 جيجابايت
# الاستخدام: bash scripts/download-model.sh
# ============================================================

set -e

MODEL_URL="https://huggingface.co/unsloth/Qwen3-1.7B-GGUF/resolve/main/Qwen3-1.7B-Q4_K_M.gguf"
MODEL_DIR="model"
MODEL_FILE="$MODEL_DIR/Qwen3-1.7B-Q4_K_M.gguf"

echo "📥 تحميل نموذج Qwen3-1.7B (Q4_K_M) - حوالي 1.1GB..."
mkdir -p "$MODEL_DIR"

if [ -f "$MODEL_FILE" ]; then
    SIZE=$(du -h "$MODEL_FILE" | cut -f1)
    echo "✅ النموذج موجود بالفعل ($SIZE) - تم التخطي"
    exit 0
fi

echo "⏳ جاري التحميل من: $MODEL_URL"
curl -L --progress-bar -o "$MODEL_FILE" "$MODEL_URL"

if [ -f "$MODEL_FILE" ]; then
    echo "✅ تم التحميل بنجاح: $(du -h "$MODEL_FILE" | cut -f1)"
else
    echo "❌ فشل التحميل"
    exit 1
fi
