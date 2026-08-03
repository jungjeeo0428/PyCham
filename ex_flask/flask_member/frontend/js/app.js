// ==========================================
// Frontend Application JavaScript (Live Server & Dynamic Host IP Supported)
// ==========================================

// 🌐 백엔드 API 서버 IP 주소 지정 (192.168.0.6 포트 5005번)
const TARGET_IP = "192.168.0.6";
const API_BASE_URL = (window.location.port === "5005" || window.location.port === "5004")
    ? ""
    : `http://${TARGET_IP}:5005`;

document.addEventListener("DOMContentLoaded", () => {
    // DOM 요소를 미리 획득
    const loginSection = document.getElementById("login-section");
    const membersSection = document.getElementById("members-section");
    const navUserInfo = document.getElementById("nav-user-info");
    const userBadge = document.getElementById("user-badge");
    const btnLogout = document.getElementById("btn-logout");
    const loginForm = document.getElementById("login-form");
    const searchForm = document.getElementById("search-form");
    const membersTbody = document.getElementById("members-tbody");
    const memberCountSpan = document.getElementById("member-count");
    const toastArea = document.getElementById("toast-area");

    // 1. 초기 세션 상태 확인 (GET /api/me)
    checkSessionState();

    function showToast(message, type = "info") {
        toastArea.innerHTML = `
            <div class="toast toast-${type}">
                <span>${message}</span>
            </div>
        `;
        setTimeout(() => {
            toastArea.innerHTML = "";
        }, 3500);
    }

    // 2. 세션 상태 확인 함수
    function checkSessionState() {
        fetch(`${API_BASE_URL}/api/me`, { credentials: "include" })
            .then(res => res.json())
            .then(data => {
                if (data.logged_in) {
                    renderLoggedInView(data.name, data.user);
                    loadMembersData();
                } else {
                    renderLoggedOutView();
                }
            })
            .catch(err => {
                console.error("API 통신 에러:", err);
                renderLoggedOutView();
            });
    }

    function renderLoggedInView(name, user) {
        loginSection.classList.add("hidden");
        membersSection.classList.remove("hidden");
        navUserInfo.classList.remove("hidden");
        userBadge.textContent = `🔑 ${name} (${user})`;
    }

    function renderLoggedOutView() {
        loginSection.classList.remove("hidden");
        membersSection.classList.add("hidden");
        navUserInfo.classList.add("hidden");
    }

    // 3. 비동기 로그인 처리 (POST /api/login)
    if (loginForm) {
        loginForm.addEventListener("submit", (e) => {
            e.preventDefault();

            const usernameVal = document.getElementById("username").value.trim();
            const passwordVal = document.getElementById("password").value.trim();

            if (!usernameVal || !passwordVal) {
                showToast("아이디와 비밀번호를 모두 입력하세요.", "danger");
                return;
            }

            fetch(`${API_BASE_URL}/api/login`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                credentials: "include",
                body: JSON.stringify({
                    username: usernameVal,
                    password: passwordVal
                })
            })
            .then(res => {
                return res.json().then(data => {
                    if (!res.ok) throw new Error(data.message || "로그인 실패");
                    return data;
                });
            })
            .then(data => {
                showToast(data.message, "success");
                renderLoggedInView(data.name, data.user);
                loadMembersData();
            })
            .catch(err => {
                showToast(err.message, "danger");
            });
        });
    }

    // 4. 로그아웃 처리 (POST /api/logout)
    if (btnLogout) {
        btnLogout.addEventListener("click", () => {
            fetch(`${API_BASE_URL}/api/logout`, { method: "POST", credentials: "include" })
                .then(res => res.json())
                .then(data => {
                    showToast(data.message, "info");
                    renderLoggedOutView();
                    loginForm.reset();
                });
        });
    }

    // 5. 회원 목록 로드 및 DOM 렌더링 (GET /api/members)
    function loadMembersData(searchQuery = "", searchType = "all") {
        let url = `${API_BASE_URL}/api/members`;
        const params = new URLSearchParams();
        if (searchQuery) params.append("search", searchQuery);
        if (searchType) params.append("search_type", searchType);

        if (params.toString()) {
            url += "?" + params.toString();
        }

        fetch(url, { credentials: "include" })
            .then(res => {
                if (!res.ok) throw new Error("회원 목록을 불러오지 못했습니다.");
                return res.json();
            })
            .then(data => {
                if (data.success) {
                    renderMembersTable(data.members);
                    memberCountSpan.textContent = data.count;
                }
            })
            .catch(err => {
                showToast(err.message, "danger");
            });
    }

    // 6. DOM 테이블 생성
    function renderMembersTable(members) {
        membersTbody.innerHTML = "";

        if (!members || members.length === 0) {
            membersTbody.innerHTML = `
                <tr>
                    <td colspan="5" class="text-center">조회 조건에 일치하는 회원 데이터가 없습니다.</td>
                </tr>
            `;
            return;
        }

        members.forEach(member => {
            const tr = document.createElement("tr");

            const memId = member.mem_id || "-";
            const memName = member.mem_name || "-";
            const memGender = member.mem_like || member.mem_job || "-";
            const memMail = member.mem_mail || member.mem_email || "-";
            const memMileage = member.mem_mileage !== undefined ? Number(member.mem_mileage).toLocaleString() + " 점" : "0 점";

            tr.innerHTML = `
                <td><strong>${memId}</strong></td>
                <td>${memName}</td>
                <td>${memGender}</td>
                <td>${memMail}</td>
                <td class="text-right mileage-text">${memMileage}</td>
            `;

            membersTbody.appendChild(tr);
        });
    }

    // 7. 검색 폼 제출
    if (searchForm) {
        searchForm.addEventListener("submit", (e) => {
            e.preventDefault();
            const searchType = document.getElementById("search_type").value;
            const searchInput = document.getElementById("search_input").value.trim();
            loadMembersData(searchInput, searchType);
        });

        const btnReset = document.getElementById("btn-reset");
        if (btnReset) {
            btnReset.addEventListener("click", () => {
                document.getElementById("search_input").value = "";
                document.getElementById("search_type").value = "all";
                loadMembersData();
            });
        }
    }
});
