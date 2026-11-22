import sys
from rich.console import Console
from rich.panel import Panel

try:
    from .bot import GeminiChatBot
except ImportError:
    from gemini_terminal_chatbot.bot import GeminiChatBot

console = Console()


def show_banner(model_name: str) -> None:
    """환영 배너 및 안내 메시지를 출력합니다."""
    banner_text = (
        f"[bold cyan]Gemini 터미널 챗봇[/bold cyan] (단일 질의응답 모드)\n\n"
        f"• 모델: [bold green]{model_name}[/bold green]\n"
        f"• 특징: [dim]대화 기록(메모리)을 유지하지 않고 매 질문을 독립적으로 처리합니다.[/dim]\n"
        f"• 명령어:\n"
        f"   [yellow]/exit[/yellow] 또는 [yellow]/quit[/yellow]  : 챗봇 종료\n"
        f"   [yellow]/help[/yellow]                 : 도움말 표시\n"
    )
    console.print(Panel(banner_text, title="🤖 Terminal Chatbot (Stateless)", border_style="cyan"))


def show_api_key_warning() -> None:
    """API 키 미설정 안내 패널을 출력합니다."""
    msg = (
        "[bold red]GEMINI_API_KEY가 설정되지 않았습니다![/bold red]\n\n"
        "1. [link=https://aistudio.google.com/apikey]Google AI Studio[/link]에서 무료 API 키를 발급받으세요.\n"
        "2. 프로젝트 루트의 [bold yellow].env[/bold yellow] 파일에 API 키를 입력하면 [cyan]python-dotenv[/cyan]를 통해 안전하게 로드됩니다:\n\n"
        "   [green]GEMINI_API_KEY=\"AIzaSy...\"[/green]\n"
    )
    console.print(Panel(msg, title="⚠️ 설정 필요", border_style="red"))


def main() -> None:
    bot = GeminiChatBot()
    show_banner(bot.model_name)

    if not bot.is_configured():
        show_api_key_warning()
        try:
            input_key = console.input("[bold yellow]지금 API 키를 입력하시겠습니까? (Enter 건너뛰기): [/bold yellow]").strip()
            if input_key:
                bot.update_api_key(input_key)
                console.print("[green]✓ API 키가 성공적으로 등록되었습니다.[/green]\n")
            else:
                console.print("[yellow].env 파일에 API 키를 설정한 후 다시 실행해 주세요.[/yellow]")
                sys.exit(1)
        except (KeyboardInterrupt, EOFError):
            console.print("\n[yellow]프로그램을 종료합니다.[/yellow]")
            sys.exit(0)

    console.print("[dim]질문을 입력하세요. 각 질문은 이전 맥락 없이 개별적으로 답변됩니다.[/dim]\n")

    while True:
        try:
            user_input = console.input("[bold blue]You > [/bold blue]").strip()
            if not user_input:
                continue

            lower_input = user_input.lower()
            if lower_input in ("/exit", "/quit", "/q"):
                console.print("[yellow]대화를 종료합니다. 좋은 하루 되세요![/yellow]")
                break

            if lower_input == "/help":
                show_banner(bot.model_name)
                continue

            # 실시간 스트리밍 답변 출력
            console.print(f"[bold purple]Gemini ({bot.model_name}) > [/bold purple]", end="")

            try:
                for chunk in bot.send_message_stream(user_input):
                    console.print(chunk, end="")
                console.print("\n")
            except Exception as e:
                console.print(f"\n[bold red]오류 발생:[/bold red] {e}\n")

        except (KeyboardInterrupt, EOFError):
            console.print("\n[yellow]대화를 종료합니다.[/yellow]")
            break


if __name__ == "__main__":
    main()
