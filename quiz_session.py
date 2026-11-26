"""퀴즈 한 판의 출제와 채점을 담당하는 QuizSession 클래스."""

import random
from datetime import datetime

from input_utils import ask_int
from quiz import CHOICE_COUNT, Quiz

# 힌트 모드에서 힌트를 요청할 때 입력하는 번호입니다.
HINT_NUMBER: int = 0
# 정답 1문제의 점수와, 힌트를 사용하고 맞혔을 때의 점수입니다.
CORRECT_POINT: float = 1.0
HINT_CORRECT_POINT: float = 0.5


class QuizSession:
    """한 판에 출제할 퀴즈를 고르고 문제를 내며, 정답 수와 점수를 계산합니다.
    게임 전체의 상태(최고 점수, 저장)는 QuizGame이 맡고, 이 클래스는 한 판의 진행만 맡습니다."""

    def __init__(self, quizzes: list[Quiz], count: int, shuffle: bool, use_hint: bool) -> None:
        if shuffle:
            # random.sample은 원본 리스트를 바꾸지 않고, 무작위로 count개를 뽑은 새 리스트를 반환합니다.
            self.quizzes: list[Quiz] = random.sample(quizzes, count)
        else:
            # 슬라이싱도 새 리스트를 만들므로 원본 순서와 내용이 유지됩니다.
            self.quizzes = quizzes[:count]
        self.use_hint: bool = use_hint  # 힌트 모드 여부
        self.correct_count: int = 0     # 맞힌 문제 수
        self.points: float = 0.0        # 획득 점수 (정답 1점, 힌트 사용 후 정답 0.5점)
        self.hints_used: int = 0        # 사용한 힌트 개수

    def ask_answer(self, quiz: Quiz) -> tuple[int, bool]:
        """정답 번호를 입력받아 (선택 번호, 힌트 사용 여부)를 반환합니다.
        힌트 모드에서는 0을 입력하면 힌트를 보여 주고 다시 입력받습니다."""
        if not self.use_hint:
            # 1 ~ CHOICE_COUNT 범위의 정수만 받도록 검증합니다.
            return ask_int("정답 번호를 입력하세요: ", 1, CHOICE_COUNT), False

        hint_shown: bool = False
        while True:
            selected: int = ask_int(
                f"정답 번호를 입력하세요 (힌트 보기: {HINT_NUMBER}): ", HINT_NUMBER, CHOICE_COUNT
            )
            if selected != HINT_NUMBER:
                return selected, hint_shown

            if not quiz.has_hint():
                print("이 문제에는 힌트가 없습니다.")
            elif hint_shown:
                # 같은 문제에서 힌트를 다시 봐도 사용 횟수는 한 번만 셉니다.
                print(f"힌트: {quiz.hint}")
            else:
                hint_shown = True
                self.hints_used += 1
                print(f"힌트: {quiz.hint} (이 문제는 맞혀도 {HINT_CORRECT_POINT}점입니다)")

    def ask_question(self, index: int, quiz: Quiz) -> None:
        """문제 하나를 출력하고 답을 입력받아 채점합니다."""
        print(f"\n[{index}/{len(self.quizzes)}]")
        quiz.display()

        selected, hint_shown = self.ask_answer(quiz)

        # check_answer()는 True 또는 False를 반환합니다.
        if quiz.check_answer(selected):
            print("정답입니다.")
            self.correct_count += 1
            # 힌트를 사용한 문제는 정답이어도 0.5점만 얻습니다.
            self.points += HINT_CORRECT_POINT if hint_shown else CORRECT_POINT
        else:
            print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

    def calculate_score(self) -> int:
        """점수 = 획득 점수 / 푼 문제 수 x 100을 반올림한 정수입니다."""
        return round(self.points / len(self.quizzes) * 100)

    def make_record(self, score: int) -> dict:
        """state.json의 history에 저장할 이번 게임 기록을 만듭니다."""
        return {
            # 게임을 마친 시각을 "YYYY-MM-DD HH:MM:SS" 형식의 문자열로 저장합니다.
            "played_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "questions_solved": len(self.quizzes),
            "correct_count": self.correct_count,
            "score": score,
            "hints_used": self.hints_used,
        }

    def run(self) -> dict:
        """모든 문제를 출제하고 결과를 출력한 뒤, 이번 게임 기록(dict)을 반환합니다."""
        # enumerate의 start=1로 문제 번호를 1부터 표시합니다.
        for index, quiz in enumerate(self.quizzes, start=1):
            self.ask_question(index, quiz)

        score: int = self.calculate_score()
        result: str = f"\n결과: {len(self.quizzes)}문제 중 {self.correct_count}문제 정답 (점수: {score}점)"
        if self.use_hint:
            result += f", 사용한 힌트 {self.hints_used}개"
        print(result)
        return self.make_record(score)
