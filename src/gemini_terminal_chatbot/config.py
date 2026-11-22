"""환경 설정 모듈: python-dotenv를 활용하여 .env 파일의 환경 변수를 안전하게 로드합니다."""

import os
from pathlib import Path
from dotenv import load_dotenv

# python-dotenv를 통한 .env 파일 로드 (프로젝트 루트 기준)
env_path = Path(__file__).resolve().parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()
DEFAULT_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.1-flash-lite").strip()

DEFAULT_SYSTEM_INSTRUCTION = (
    "당신은 친절하고 유능한 터미널 AI 어시스턴트입니다. "
    "사용자의 질문에 명확하고 간결하며 도움이 되는 답변을 한국어로 제공합니다. "
    "코드나 서식은 마크다운을 적절히 활용하여 작성하세요."
)
