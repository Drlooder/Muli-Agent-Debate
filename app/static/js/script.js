lucide.createIcons();

function startDebateSim() {
    const input = document.getElementById('topic-input');
    if(!input.value.trim()) return;
    
    // Visual feedback indicator for preview
    const btn = document.querySelector('.btn-cyber');
    const originalHTML = btn.innerHTML;
    btn.innerHTML = `<i data-lucide="loader-2" class="w-4 h-4 animate-spin"></i> Processing...`;
    lucide.createIcons();
    
    setTimeout(() => {
        btn.innerHTML = originalHTML;
        lucide.createIcons();
    }, 1200);
}

document.addEventListener("DOMContentLoaded", () => {
    const toggleBtn = document.getElementById("toggleResponsesBtn");
    const responsesPanel = document.getElementById("responsesPanel");

    toggleBtn.addEventListener("click", () => {
        responsesPanel.classList.toggle("is-hidden");
        toggleBtn.classList.toggle("is-collapsed");
    });
});