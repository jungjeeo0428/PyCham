# ============================================================
# 설정 파일 — 모든 실습이 이 파일을 불러다 씁니다.
# README.md의 준비 단계를 마친 뒤 아래 두 값을 채워 넣으세요!
# pip install "notion-client==2.2.1" pandas openpyxl
# ============================================================
import os
# API 시크릿 key (ntn_ 또는 secret_ 으로 시작)
NOTION_TOKEN = os.getenv("Notion_PAT")
# 실습용 페이지 ID (URL 맨 뒤 32자리)
PARENT_PAGE_ID = "3a7590e6979880d9ab0fd29df81aeb4d"
# ------------------------------------------------------------
# 아래는 건드리지 않아도 됩니다 (공용 연결 코드)
# ------------------------------------------------------------
from notion_client import Client
def connect_notion() -> Client:
    if NOTION_TOKEN == "여기에_토큰_붙여넣기":
        raise SystemExit("⚠️config.py 를 열어 NOTION_TOKEN 부터 채워주세요! (README 참고)")
    return Client(auth=NOTION_TOKEN)
