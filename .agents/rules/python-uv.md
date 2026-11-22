---
trigger: model_decision
description: "Python 환경 설정, 가상환경 생성, 패키지 관리 및 스크립트 실행 시 uv 사용 강제 규칙"
---

# Python 도구 규칙: uv 필수 사용

이 프로젝트의 모든 Python 관련 작업에는 반드시 **`uv`**를 사용합니다. 일반 `pip`, `python -m venv`, `conda`는 직접 사용하지 않습니다.

- **가상환경 생성:** `uv venv` 사용 (예: `uv venv --python 3.12`) — `python -m venv` 금지
- **Python 설치:** `uv python install <version>` 사용
- **패키지 설치:** `uv pip install <pkg>` 또는 `uv add <pkg>` 사용 — 단독 `pip install` 금지
- **스크립트 실행:** `.venv` 활성화 후 실행하거나 `uv run python <script.py>` 사용
- **CLI 도구 실행:** `uvx <tool>` 사용
