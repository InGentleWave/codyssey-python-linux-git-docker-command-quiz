"""퀴즈 게임 실행 진입점."""
# state.json 저장과 불러오기 함수를 가져옵니다.
from storage import load_state, save_state
# Quiz 클래스와 선택지 개수를 가져옵니다.
from quiz import CHOICE_COUNT, Quiz
# 숫자 입력을 검증하는 함수를 가져옵니다.
from input_utils import ask_int
# 문자 입력을 검증하는 함수를 가져옵니다.
from input_utils import ask_text

# 
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

def add_quiz(quizzes: list[Quiz]) -> None:
    """문제, 선택지 4개, 정답 번호를 입력받아 Quiz를 만들고 목록 끝에 추가합니다."""
    # 빈 문제는 허용하지 않으므로 ask_text로 입력받습니다.
    question: str = ask_text("문제를 입력하세요: ")

    # 선택지는 CHOICE_COUNT(4)개를 모두 빈 값 없이 입력받습니다.
    choices: list[str] = []
    for number in range(1, CHOICE_COUNT + 1):
        choice: str = ask_text(f"선택지 {number}번: ")
        choices.append(choice)

    # 정답 번호는 1 ~ CHOICE_COUNT 범위의 정수만 받습니다.
    answer: int = ask_int("정답 번호를 입력하세요 (1~4): ", 1, CHOICE_COUNT)

    # 전달받은 리스트에 직접 추가하므로 run()의 quizzes에도 반영됩니다.
    quizzes.append(Quiz(question, choices, answer))
    print("퀴즈가 추가되었습니다.")

def show_quiz_list(quizzes: list[Quiz]) -> None:
    """저장된 퀴즈를 번호 순서대로 출력하고, 각 퀴즈의 정답 번호도 함께 보여줍니다."""
    # 퀴즈가 없으면 목록을 보여줄 수 없으므로 안내 후 메뉴로 돌아갑니다 (설계 6절 4번 3항).
    if len(quizzes) == 0:
        print("등록된 퀴즈가 없습니다. 퀴즈를 먼저 추가해 주세요.")
        return

    total: int = len(quizzes)

    # enumerate의 start=1로 목록 번호를 1부터 표시합니다.
    for index, quiz in enumerate(quizzes, start=1):
        print(f"\n[{index}/{total}]")
        # 문제와 선택지를 출력합니다. 기존 Quiz.display()를 그대로 사용합니다.
        quiz.display()
        # 목록에서는 정답 번호를 함께 노출합니다.
        print(f"정답: {quiz.answer}번")

def run():
    """메뉴를 반복 출력하고 선택된 번호를 처리합니다."""
    # state.json에서 저장된 데이터를 불러옵니다. 없거나 손상되었으면 기본 데이터를 사용합니다.
    quizzes, best_score, history = load_state()
        
    # 퀴즈가 존재하지 않는 경우를 테스트하기 위한 코드입니다. 실제로는 퀴즈를 가져오므로 주석 처리합니다.
    # quizzes = []  # 테스트용: 퀴즈가 없는 경우를 확인하려면 이 줄을 주석 해제합니다.

    try:
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

            # 2번 메뉴는 퀴즈 추가를 실행합니다.
            elif choice == 2:
                add_quiz(quizzes)
                # 퀴즈 추가한 후에는 state.json에 저장합니다. 저장 실패 시 안내만 출력하고 계속 진행합니다.
                save_state(quizzes, best_score, history)  # 최고 점수와 기록은 기존 값을 전달합니다.

            elif choice == 3:
                # 퀴즈 목록을 출력합니다.
                show_quiz_list(quizzes)
            else:
                # 4번 기능은 설계 8.2의 #6~9에서 구현할 예정이므로 안내 문구만 출력합니다.
                print("이 메뉴는 아직 구현되지 않았습니다.")
    finally:
        # 프로그램 종료 시 state.json에 저장합니다. 저장 실패 시 안내만 출력하고 종료합니다.
        save_state(quizzes, best_score, history)


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