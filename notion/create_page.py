# ============================================================
# 02. 페이지 만들기 — 파이썬이 Notion에 글을 씁니다!
# ------------------------------------------------------------
# 페이지 생성(Create), 다양한 블록(제목/글/체크박스/콜아웃)
# ============================================================
import sys
sys.stdout.reconfigure(encoding="utf-8")
import csv
from notion_client import Client

from datetime import date
from config import connect_notion, PARENT_PAGE_ID

notion = connect_notion()
# ------------------------------------------------------------
# 페이지 만들기: "어디에(parent) + 제목(properties) + 내용(children)"
# 블록 = Notion 화면의 한 줄 한 줄 (문단, 제목, 체크박스 ...)
# ------------------------------------------------------------
새페이지 = notion.pages.create(
    # [1] 어디에 만들까? → 실습용 페이지 아래에
    parent={"page_id": PARENT_PAGE_ID},
    # [2] 페이지 제목
    properties={
        "title": [{"text": {"content": f"🤖 파이썬이 만든 페이지 ({date.today()})"}}]
    },
    # [3] 페이지 내용 (블록 목록)
    children=[
        {   # 큰 제목
            "heading_1": {
                "rich_text": [{"text": {"content": "안녕하세요, 저는 파이썬입니다"}}]
            }
        },
        {   # 일반 문단
            "paragraph": {
                "rich_text": [{"text": {"content": "이 페이지는 사람이 아니라 코드가 만들었습니다!"}}]
            }
        },
        {   # 콜아웃 (강조 박스)
            "callout": {
                "icon": {"emoji": "💡"},
                "rich_text": [{"text": {"content": "코드 몇 줄이면 매일 반복하는 Notion 정리를 자동화할 수 있어요."}}]
            }
        },
        {   # 체크박스 (할 일)
            "to_do": {
                "rich_text": [{"text": {"content": "파이썬으로 페이지 만들기"}}],
                "checked": True,   # 이미 완료!
            }
        },
        {
            "to_do": {
                "rich_text": [{"text": {"content": "다음 실습: 테이블 만들기"}}],
                "checked": False,
            }
        },
    ],
)
print("🎉 페이지 생성 완료! Notion을 열어 확인해 보세요!")
print(f"   바로가기: {새페이지['url']}")
# ------------------------------------------------------------
# 💪 직접 해보기 (연습문제)
#  이전 실습에서 사용한 csv 정보를 page로 만들어보세요!
# ------------------------------------------------------------
csv_file_path = "C:/medicalAI/Pycham/crowling/student_list.csv"
table_rows = []
with open(csv_file_path, encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        cells = [[{"type": "text", "text": {"content": cell}}] for cell in row]
        table_rows.append({
            "type": "table_row",
            "table_row": {"cells": cells}
        })

New_page_title = "csv 데이터 결과"
column_count = len(table_rows[0]["table_row"]["cells"]) if table_rows else 1
새페이지 = notion.pages.create(
    # [1] 어디에 만들까? → 실습용 페이지 아래에
    parent={"page_id": '3a7590e6979880d9ab0fd29df81aeb4d'},
    # [2] 페이지 제목
    properties={
        "title": [{"text": {"content": f"🤖 csv파일 넣기 연습 ({date.today()})"}}]
    },
    # [3] 페이지 내용 (블록 목록)
    children=[
        {   # 큰 제목
            "heading_1": {
                "rich_text": [{"text": {"content": "파일 파이썬으로 업로드하기"}}]
            }
        },
        {   # 일반 문단
            "paragraph": {
                "rich_text": [{"text": {"content": "이 페이지는 사람이 아니라 코드가 만들었습니다!"}}]
            }
        },
        {   # 콜아웃 (강조 박스)
            "callout": {
                "icon": {"emoji": "💡"},
                "rich_text": [{"text": {"content": "코드 몇 줄이면 매일 반복하는 Notion 정리를 자동화할 수 있어요."}}]
            }
        },
        {
            "object": "block",
            "type": "table",
            "table": {
                "table_width": column_count,    # 표의 열(컬럼) 개수
                "has_column_header": True,       # 첫 번째 행을 헤더(제목)로 지정
                "children": table_rows           # 읽어온 CSV 행 데이터들
            }
        }

    ],
)
print("🎉 페이지 생성 완료! Notion을 열어 확인해 보세요!")
print(f"   바로가기: {새페이지['url']}")