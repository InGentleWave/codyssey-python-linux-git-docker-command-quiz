"""퀴즈 게임 실행 진입점."""
# 기본 퀴즈 데이터를 가져옵니다.
from default_quizzes import get_default_quizzes
# Quiz 클래스와 선택지 개수를 가져옵니다.
from quiz import CHOICE_COUNT
# 숫자 입력을 검증하는 함수를 가져옵니다.
from input_utils import ask_int

# 메뉴 항목 목록입니다. 순서대로 1번, 2번, ... 이 됩니다.
MENU_ITEMS = [
    "퀴즈 풀기",
    "퀴즈 추가",
    "퀴즈 목록",
    "점수 확인",
    "종료",
]
# 마지막 항목(종료)의 번호입니다. 항목 개수가 바뀌어도 자동으로 맞춰집니다.
EXIT_NUMBER = len(MENU_ITEMS)


def show_menu():
    """메뉴 목록을 출력합니다."""
    print("\n=== 나만의 퀴즈 게임 ===")
    # enumerate의 start=1로 메뉴 번호를 1부터 붙여 출력합니다.
    for number, label in enumerate(MENU_ITEMS, start=1):
        print(f"{number}. {label}")

def play_quiz(quizzes):
    """퀴즈를 원본 순서대로 전부 출제하고 정답 수와 점수를 출력합니다."""
    total = len(quizzes)

    # 퀴즈가 없으면 풀 수 없으므로 안내 후 메뉴로 돌아갑니다.
    if total == 0:
        print("등록된 퀴즈가 없습니다. 퀴즈를 먼저 추가해 주세요.")
        return

    correct_count = 0

    # enumerate의 start=1로 문제 번호를 1부터 표시합니다.
    for index, quiz in enumerate(quizzes, start=1):
        print(f"\n[{index}/{total}]")
        quiz.display()

        # 1 ~ CHOICE_COUNT 범위의 정수만 받도록 검증합니다.
        selected = ask_int("정답 번호를 입력하세요: ", 1, CHOICE_COUNT)

        # check_answer()는 True 또는 False를 반환합니다.
        if quiz.check_answer(selected):
            print("정답입니다.")
            correct_count += 1
        else:
            print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

    # 설계 5절의 점수 계산식: 획득 점수 합계 / 푼 문제 수 x 100, 반올림하여 정수로 저장
    # 힌트 기능이 없으므로 정답 1점, 오답 0점으로 합계와 정답 수가 같습니다.
    score = round(correct_count / total * 100)
    print(f"\n결과: {total}문제 중 {correct_count}문제 정답 (점수: {score}점)")

def run():
    """메뉴를 반복 출력하고 선택된 번호를 처리합니다."""
    # 프로그램 시작 시 기본 퀴즈 목록을 한 번 만듭니다.
    quizzes = get_default_quizzes()

    # 퀴즈가 존재하지 않는 경우를 테스트하기 위한 코드입니다. 실제로는 기본 퀴즈를 가져오므로 주석 처리합니다.
    quizzes = []  # 테스트용: 퀴즈가 없는 경우를 확인하려면 이 줄을 주석 해제합니다.
    
    # 종료를 선택할 때까지 메뉴를 계속 보여줍니다.
    while True:
        show_menu()
        # 1 ~ EXIT_NUMBER 범위의 정수만 받도록 검증합니다.
        choice = ask_int("메뉴 번호를 입력하세요: ", 1, EXIT_NUMBER)

        # 종료를 선택하면 반복을 빠져나와 프로그램을 끝냅니다.
        if choice == EXIT_NUMBER:
            print("프로그램을 종료합니다.")
            break

        # 1번 메뉴는 퀴즈 풀기를 실행합니다.
        if choice == 1:
            play_quiz(quizzes)
        else:
            # 2~4번 기능은 설계 8.2의 #6~9에서 구현할 예정이므로 안내 문구만 출력합니다.
            print("이 메뉴는 아직 구현되지 않았습니다.")


# 이 파일을 직접 실행했을 때만 아래 코드가 동작합니다 (다른 파일에서 import하면 실행되지 않음).
if __name__ == "__main__":
    try:
        run()
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