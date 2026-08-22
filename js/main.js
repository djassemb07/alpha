// ===== Alpha — سكربت الموقع =====

// تأثير الزر الرئيسي
const ctaBtn = document.getElementById("cta-btn");
const clickMsg = document.getElementById("click-msg");

if (ctaBtn && clickMsg) {
  ctaBtn.addEventListener("click", () => {
    clickMsg.textContent = "🎉 أهلاً بك! هذا الموقع جاهز للتطوير.";
    clickMsg.classList.remove("hidden");

    // إخفاء الرسالة بعد بضع ثوانٍ
    setTimeout(() => {
      clickMsg.classList.add("hidden");
    }, 4000);
  });
}

// إظهار السنة الحالية تلقائيًا في الفوتر
document.addEventListener("DOMContentLoaded", () => {
  const yearEl = document.querySelector(".footer p");
  if (yearEl) {
    yearEl.innerHTML = `© ${new Date().getFullYear()} Alpha — صُنع بحب ❤️`;
  }
});
