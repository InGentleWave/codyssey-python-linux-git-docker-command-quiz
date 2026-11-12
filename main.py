"""퀴즈 게임 실행 진입점."""

# 퀴즈 게임 클래스를 가져옵니다.
from quiz_game import QuizGame

# 이 파일을 직접 실행했을 때만 아래 코드가 동작합니다 (다른 파일에서 import하면 실행되지 않음).
if __name__ == "__main__":
    try:
        QuizGame().run()
    except KeyboardInterrupt:
        # Ctrl+C 입력 시 안내 후 정상 종료합니다.
        print("\n입력이 중단되어 프로그램을 종료합니다.")
    except EOFError:
        # 입력 스트림이 끝난 경우(예: Ctrl+D) 안내 후 정상 종료합니다.
        print("\n입력이 종료되어 프로그램을 종료합니다.")
    except Exception as error:
        # 예상하지 못한 오류가 나면 내용을 출력합니다.
        print(f"오류가 발생했습니다: {error}")
        # 바로 창이 닫히지 않도록 Enter 입력을 기다린 뒤 종료합니다.
        input("Enter를 누르면 종료합니다...")