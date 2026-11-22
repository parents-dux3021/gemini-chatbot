from typing import Iterator, Optional
from google import genai
from google.genai import types

from .config import DEFAULT_MODEL, DEFAULT_SYSTEM_INSTRUCTION, GEMINI_API_KEY


class GeminiChatBot:
    """메모리(대화 기록) 없이 단일 턴 질의응답을 처리하는 Gemini 챗봇 클래스"""

    def __init__(
        self,
        api_key: Optional[str] = None,
        model_name: Optional[str] = None,
        system_instruction: Optional[str] = None,
    ):
        self.api_key = api_key or GEMINI_API_KEY
        self.model_name = model_name or DEFAULT_MODEL
        self.system_instruction = system_instruction or DEFAULT_SYSTEM_INSTRUCTION
        self.client = genai.Client(api_key=self.api_key) if self.api_key else None

    def is_configured(self) -> bool:
        """API 키가 설정되었는지 확인합니다."""
        return bool(self.api_key and self.client)

    def update_api_key(self, api_key: str) -> None:
        """새 API 키로 클라이언트를 재초기화합니다."""
        self.api_key = api_key.strip()
        self.client = genai.Client(api_key=self.api_key)

    def send_message_stream(self, message: str) -> Iterator[str]:
        """
        메모리(이전 대화 맥락)를 저장하지 않고, 
        현재 입력된 메시지에 대해서만 실시간 청크 단위로 스트리밍 답변을 생성합니다.
        """
        if not self.is_configured():
            raise ValueError("GEMINI_API_KEY가 설정되지 않았습니다.")

        config = types.GenerateContentConfig(
            system_instruction=self.system_instruction,
            temperature=0.7,
        )

        response_stream = self.client.models.generate_content_stream(
            model=self.model_name,
            contents=message,
            config=config,
        )

        for chunk in response_stream:
            if chunk.text:
                yield chunk.text
