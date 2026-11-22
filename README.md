# 🤖 Gemini Terminal Chatbot (Stateless)

Google Gemini 무료 티어 모델(`gemini-3.1-flash-lite`)과 최신 `google-genai` SDK를 활용한 터미널 챗봇입니다.

## ✨ 주요 특징
- **메모리 없는 단일 질의응답 (Stateless)**: 이전 대화 기록을 저장하지 않고, 매 턴마다 입력된 질문에 대해 독립적으로 신속하게 응답
- **최신 Gemini 모델**: 무료 티어로 빠르게 사용 가능한 `gemini-3.1-flash-lite` 적용
- **실시간 스트리밍**: 토큰 생성 즉시 실시간 텍스트 출력
- **Rich 터미널 UI**: 가독성 높은 색상과 패널 출력
- **python-dotenv를 통한 안전한 API 키 관리**: `.env` 파일과 `python-dotenv`를 사용하여 코드에 노출 없이 `GEMINI_API_KEY`를 안전하게 로드
- **uv 초고속 패키지 관리**: 가상환경 및 의존성 관리

---

## 🚀 시작하기

### 1. API 키 설정
[Google AI Studio](https://aistudio.google.com/apikey)에서 무료 API 키를 발급받은 후, 프로젝트 폴더 내 `.env` 파일에 입력합니다.

```env
GEMINI_API_KEY="여러분의_GEMINI_API_KEY"
GEMINI_MODEL="gemini-3.1-flash-lite"
```

### 2. 실행 방법

`ch05/gemini-terminal-chatbot` 폴더에서 아래 명령어 실행:

```powershell
uv run gemini-terminal-chatbot
```
*(또는 `uv run python -m gemini_terminal_chatbot.main`)*

---

## ⌨️ 지원 명령어
- `/help`: 안내 및 도움말 출력
- `/exit` 또는 `/quit`: 챗봇 종료
