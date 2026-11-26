"""퀴즈 한 판의 출제와 채점을 담당하는 QuizSession 클래스."""

from input_utils import ask_int
from quiz import CHOICE_COUNT, Quiz


class QuizSession:
    """한 판에 출제할 퀴즈 목록을 받아 문제를 내고, 정답 수와 점수를 계산합니다.
    게임 전체의 상태(최고 점수, 저장)는 QuizGame이 맡고, 이 클래스는 한 판의 진행만 맡습니다."""

    def __init__(self, quizzes: list[Quiz]) -> None:
        # 원본 목록이 바뀌지 않도록 복사해서 저장합니다.
        self.quizzes: list[Quiz] = list(quizzes)
        self.correct_count: int = 0  # 맞힌 문제 수

    def ask_question(self, index: int, quiz: Quiz) -> None:
        """문제 하나를 출력하고 답을 입력받아 채점합니다."""
        print(f"\n[{index}/{len(self.quizzes)}]")
        quiz.display()

        # 1 ~ CHOICE_COUNT 범위의 정수만 받도록 검증합니다.
        selected: int = ask_int("정답 번호를 입력하세요: ", 1, CHOICE_COUNT)

        # check_answer()는 True 또는 False를 반환합니다.
        if quiz.check_answer(selected):
            print("정답입니다.")
            self.correct_count += 1
        else:
            print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

    def calculate_score(self) -> int:
        """점수 = 정답 수 / 푼 문제 수 x 100을 반올림한 정수입니다."""
        return round(self.correct_count / len(self.quizzes) * 100)

    def run(self) -> int:
        """모든 문제를 출제하고 결과를 출력한 뒤 점수를 반환합니다."""
        # enumerate의 start=1로 문제 번호를 1부터 표시합니다.
        for index, quiz in enumerate(self.quizzes, start=1):
            self.ask_question(index, quiz)

        score: int = self.calculate_score()
        print(f"\n결과: {len(self.quizzes)}문제 중 {self.correct_count}문제 정답 (점수: {score}점)")
        return score
