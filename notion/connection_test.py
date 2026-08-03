# ============================================================
# 01. 연결 테스트
# ------------------------------------------------------------
# API 연결 확인, 페이지 정보 읽기(조회)
# ============================================================
import sys
sys.stdout.reconfigure(encoding="utf-8")
from config import connect_notion, PARENT_PAGE_ID
notion = connect_notion()

나 = notion.users.me()
print(f"연결 성공! 봇 이름: {나['name']}")
# ------------------------------------------------------------
# 실습용 페이지 읽어오기 (조회 = Read)
# ------------------------------------------------------------
페이지 = notion.pages.retrieve(page_id=PARENT_PAGE_ID)
제목조각 = 페이지["properties"]["title"]["title"]
제목 = 제목조각[0]["plain_text"] if 제목조각 else "(제목 없음)"
print(f"✅ 페이지 읽기 성공!")
print(f"   제목: {제목}")
print(f"   생성일: {페이지['created_time'][:10]}")
print(f"   주소: {페이지['url']}")
# ------------------------------------------------------------
# 페이지 안의 내용(블록) 읽어오기
# ------------------------------------------------------------
블록들 = notion.blocks.children.list(block_id=PARENT_PAGE_ID)
print(f"\n📄 페이지 안에 블록이 {len(블록들['results'])}개 있습니다:")
for 블록 in 블록들["results"]:
    print(f"   - 종류: {블록['type']}")