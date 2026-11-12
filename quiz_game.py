"""퀴즈 게임의 상태와 기능을 묶어 관리하는 QuizGame 클래스."""

# 퀴즈 객체와 선택지 개수를 가져옵니다.
from quiz import CHOICE_COUNT, Quiz
# 숫자 입력과 텍스트 입력을 검증하는 함수를 가져옵니다.
from input_utils import ask_int, ask_text
# state.json 저장과 불러오기 함수를 가져옵니다.
from storage import load_state, save_state

# 메뉴 항목 목록입니다. 순서대로 1번, 2번, ... 이 됩니다.
MENU_ITEMS: list[str] = [
    "퀴즈 풀기",
    "퀴즈 추가",
    "퀴즈 목록",
    "점수 확인",
    "종료",
]
# 마지막 항목(종료)의 번호입니다. 항목 개수가 바뀌어도 자동으로 맞춰집니다.
EXIT_NUMBER: int = len(MENU_ITEMS)


class QuizGame:
    """퀴즈 목록, 최고 점수, 기록을 가지고 메뉴 기능을 실행하는 클래스 (설계 4.2절)."""

    def __init__(self) -> None:
        # state.json에서 저장된 데이터를 불러와 인스턴스 속성에 담습니다.
        quizzes, best_score, history = load_state()

        # 퀴즈가 존재하지 않는 경우를 테스트하기 위한 코드입니다. 실제로는 퀴즈를 가져오므로 주석 처리합니다.
        # quizzes = []  # 테스트용: 퀴즈가 없는 경우를 확인하려면 이 줄을 주석 해제합니다.
        
        self.quizzes: list[Quiz] = quizzes        # 퀴즈 목록
        self.best_score: int | None = best_score  # 최고 점수 (None이면 아직 풀지 않음)
        self.history: list[dict] = history        # 게임 기록 (8.2 #16에서 채워짐)

    def save(self) -> None:
        """현재 퀴즈 목록, 최고 점수, 기록을 state.json에 저장합니다."""
        save_state(self.quizzes, self.best_score, self.history)

    def show_menu(self) -> None:
        """메뉴 목록을 출력합니다."""
        print("\n=== 나만의 퀴즈 게임 ===")
        # enumerate의 start=1로 메뉴 번호를 1부터 붙여 출력합니다.
        for number, label in enumerate(MENU_ITEMS, start=1):
            print(f"{number}. {label}")

    def play_quiz(self) -> None:
        """퀴즈를 원본 순서대로 전부 출제하고, 점수를 계산해 최고 점수를 갱신합니다."""
        total: int = len(self.quizzes)

        # 퀴즈가 없으면 풀 수 없으므로 안내 후 메뉴로 돌아갑니다.
        if total == 0:
            print("등록된 퀴즈가 없습니다. 퀴즈를 먼저 추가해 주세요.")
            return

        correct_count: int = 0

        # enumerate의 start=1로 문제 번호를 1부터 표시합니다.
        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"\n[{index}/{total}]")
            quiz.display()

            # 1 ~ CHOICE_COUNT 범위의 정수만 받도록 검증합니다.
            selected: int = ask_int("정답 번호를 입력하세요: ", 1, CHOICE_COUNT)

            # check_answer()는 True 또는 False를 반환합니다.
            if quiz.check_answer(selected):
                print("정답입니다.")
                correct_count += 1
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

        # 설계 5절의 점수 계산식: 정답 수 / 푼 문제 수 x 100, 반올림하여 정수로 저장
        # 힌트 기능이 없으므로 정답 1점, 오답 0점입니다.
        score: int = round(correct_count / total * 100)
        print(f"\n결과: {total}문제 중 {correct_count}문제 정답 (점수: {score}점)")

        # 아직 풀지 않았거나(None) 기존 최고 점수보다 높으면 갱신합니다 (설계 6절 4번 1항).
        if self.best_score is None or score > self.best_score:
            self.best_score = score
            print("최고 점수를 갱신했습니다.")

    def add_quiz(self) -> None:
        """문제, 선택지 4개, 정답 번호를 입력받아 Quiz를 추가하고 바로 저장합니다."""
        # 빈 문제는 허용하지 않으므로 ask_text로 입력받습니다.
        question: str = ask_text("문제를 입력하세요: ")

        # 선택지는 CHOICE_COUNT(4)개를 모두 빈 값 없이 입력받습니다.
        choices: list[str] = []
        for number in range(1, CHOICE_COUNT + 1):
            choice: str = ask_text(f"선택지 {number}번: ")
            choices.append(choice)

        # 정답 번호는 1 ~ CHOICE_COUNT 범위의 정수만 받습니다.
        answer: int = ask_int(f"정답 번호를 입력하세요 (1~{CHOICE_COUNT}): ", 1, CHOICE_COUNT)

        self.quizzes.append(Quiz(question, choices, answer))
        print("퀴즈가 추가되었습니다.")

        # 퀴즈를 추가할 때마다 바로 저장합니다 (설계 6절 4번 2항).
        self.save()

    def show_quiz_list(self) -> None:
        """저장된 퀴즈를 번호 순서대로 출력하고, 각 퀴즈의 정답 번호도 함께 보여줍니다."""
        # 퀴즈가 없으면 안내 후 메뉴로 돌아갑니다 (설계 6절 4번 3항).
        if len(self.quizzes) == 0:
            print("등록된 퀴즈가 없습니다. 퀴즈를 먼저 추가해 주세요.")
            return

        total: int = len(self.quizzes)

        # enumerate의 start=1로 목록 번호를 1부터 표시합니다.
        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"\n[{index}/{total}]")
            quiz.display()
            print(f"정답: {quiz.answer}번")

    def show_best_score(self) -> None:
        """최고 점수를 출력합니다. 아직 풀지 않았으면 안내 문구를 출력합니다 (설계 6절 4번 4항)."""
        # None은 한 번도 풀지 않은 상태입니다. 0점은 정상 점수이므로 None과 구분합니다.
        if self.best_score is None:
            print("아직 퀴즈를 푼 기록이 없습니다.")
            return
        print(f"최고 점수: {self.best_score}점")

    def run(self) -> None:
        """메뉴를 반복 출력하고 선택된 번호를 처리합니다. 종료 시 항상 저장합니다."""
        # try/finally로 감싸면 정상 종료, Ctrl+C, EOF 중 어떤 경우에도 마지막에 저장됩니다 (설계 6절 5번).
        try:
            while True:
                self.show_menu()
                # 1 ~ EXIT_NUMBER 범위의 정수만 받도록 검증합니다.
                choice: int = ask_int("메뉴 번호를 입력하세요: ", 1, EXIT_NUMBER)

                # 종료를 선택하면 반복을 빠져나와 프로그램을 끝냅니다.
                if choice == EXIT_NUMBER:
                    print("프로그램을 종료합니다.")
                    break
                # 1번 메뉴는 퀴즈 풀기를 실행합니다.
                if choice == 1:
                    self.play_quiz()
                # 2번 메뉴는 퀴즈 추가를 실행합니다.
                elif choice == 2:
                    self.add_quiz()
                # 3번 메뉴는 퀴즈 목록을 출력합니다.
                elif choice == 3:
                    self.show_quiz_list()
                # 4번 메뉴는 최고 점수를 출력합니다.
                elif choice == 4:
                    self.show_best_score()
        finally:
            self.save()