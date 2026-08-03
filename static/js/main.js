// ==========================================
// Member Portal Client Script (Vanilla JS)
// ==========================================

document.addEventListener("DOMContentLoaded", () => {
    // 1. 로그인 폼 유효성 검사
    const loginForm = document.getElementById("login-form");
    if (loginForm) {
        loginForm.addEventListener("submit", (e) => {
            const userInput = document.getElementById("username");
            const passInput = document.getElementById("password");

            if (!userInput.value.trim()) {
                alert("아이디를 입력해 주세요.");
                userInput.focus();
                e.preventDefault();
                return;
            }

            if (!passInput.value.trim()) {
                alert("비밀번호를 입력해 주세요.");
                passInput.focus();
                e.preventDefault();
                return;
            }
        });
    }

    // 2. 알림 메시지 3초 후 자동 감춤 처리
    const alertBox = document.querySelector(".alert");
    if (alertBox) {
        setTimeout(() => {
            alertBox.style.transition = "opacity 0.5s ease";
            alertBox.style.opacity = "0";
            setTimeout(() => {
                alertBox.remove();
            }, 500);
        }, 3500);
    }
});
