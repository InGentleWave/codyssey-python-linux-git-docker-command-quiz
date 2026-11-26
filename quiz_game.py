"""퀴즈 게임의 상태와 기능을 묶어 관리하는 QuizGame 클래스."""

# 퀴즈 객체와 선택지 개수를 가져옵니다.
from quiz import CHOICE_COUNT, Quiz
# 숫자 입력과 텍스트 입력을 검증하는 함수를 가져옵니다.
from input_utils import ask_int, ask_optional_text, ask_text
# 한 판의 출제와 채점을 담당하는 클래스를 가져옵니다.
from quiz_session import QuizSession
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

# 퀴즈 풀기 모드 목록입니다. 각 항목은 (화면에 보일 이름, 문제 순서를 섞을지 여부, 힌트 사용 여부)입니다.
PLAY_MODES: list[tuple[str, bool, bool]] = [
    ("기본 (저장된 순서대로 출제)", False, False),
    ("랜덤 (순서를 섞어 출제)", True, False),
    ("기본 + 힌트", False, True),
    ("랜덤 + 힌트", True, True),
]


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

    def choose_mode(self) -> tuple[str, bool, bool]:
        """퀴즈 풀기 모드 목록을 출력하고, 선택한 모드를 반환합니다."""
        print("\n풀이 모드를 선택하세요. (힌트 모드: 힌트를 본 문제는 맞혀도 0.5점)")
        for number, (label, _, _) in enumerate(PLAY_MODES, start=1):
            print(f"{number}. {label}")
        choice: int = ask_int("모드 번호를 입력하세요: ", 1, len(PLAY_MODES))
        # 화면 번호는 1부터, 리스트 인덱스는 0부터이므로 1을 뺍니다.
        return PLAY_MODES[choice - 1]

    def play_quiz(self) -> None:
        """모드와 문제 수를 입력받아 퀴즈 한 판을 진행하고, 결과 점수로 최고 점수를 갱신합니다."""
        total: int = len(self.quizzes)

        # 퀴즈가 없으면 풀 수 없으므로 안내 후 메뉴로 돌아갑니다.
        if total == 0:
            print("등록된 퀴즈가 없습니다. 퀴즈를 먼저 추가해 주세요.")
            return

        mode_label, shuffle, use_hint = self.choose_mode()
        # 0개나 전체 퀴즈 수를 넘는 값은 ask_int가 안내 후 다시 입력받습니다.
        count: int = ask_int(f"풀 문제 수를 입력하세요 (1~{total}): ", 1, total)
        print(f"\n[{mode_label}] {count}문제를 시작합니다.")

        # 출제와 채점은 QuizSession이 담당합니다.
        score: int = QuizSession(self.quizzes, count, shuffle, use_hint).run()

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

        # 힌트는 선택 항목입니다. 그냥 Enter를 누르면 None(힌트 없음)이 됩니다.
        hint: str | None = ask_optional_text("힌트를 입력하세요 (없으면 Enter): ")

        self.quizzes.append(Quiz(question, choices, answer, hint))
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
            if quiz.has_hint():
                print(f"힌트: {quiz.hint}")

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