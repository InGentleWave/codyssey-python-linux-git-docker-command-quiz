"""퀴즈 한 문항을 표현하는 Quiz 클래스."""

# 선택지 개수는 4개로 고정합니다 (설계 4.1절).
CHOICE_COUNT: int = 4


class Quiz:
    """문제, 선택지 4개, 정답 번호(1~4), 힌트(선택)를 가진 퀴즈 한 문항."""

    def __init__(self, question : str, choices : list[str], answer : int, hint : str | None = None) -> None:
        # 선택지 개수가 4개가 아니면 잘못된 데이터이므로 예외를 발생시킵니다.
        if len(choices) != CHOICE_COUNT:
            raise ValueError(f"선택지는 {CHOICE_COUNT}개여야 합니다.")
        # 정답 번호는 1~4 범위의 정수여야 합니다.
        if not 1 <= answer <= CHOICE_COUNT:
            raise ValueError(f"정답 번호는 1부터 {CHOICE_COUNT} 사이여야 합니다.")
        # 힌트는 없거나(None) 문자열이어야 합니다.
        if hint is not None and not isinstance(hint, str):
            raise ValueError("힌트는 문자열이어야 합니다.")
        self.question = question          # 문제 문장
        self.choices = list(choices)      # 원본 리스트가 바뀌지 않도록 복사해서 저장
        self.answer = answer              # 정답 번호 (1~4)
        self.hint = hint                  # 힌트 문구 (None이면 힌트 없음)

    def has_hint(self) -> bool:
        """힌트가 있으면 True를 반환합니다."""
        return self.hint is not None

    def display(self)-> None:
        """문제와 번호가 붙은 선택지를 화면에 출력합니다."""
        print(self.question)
        # enumerate의 start=1로 선택지 번호를 1부터 붙입니다.
        for number, choice in enumerate(self.choices, start=1):
            print(f"  {number}. {choice}")

    def check_answer(self, selected : int) -> bool:
        """입력된 번호가 정답이면 True, 아니면 False를 반환합니다."""
        return selected == self.answer

    def to_dict(self) -> dict:
        """state.json 저장용 dict로 변환합니다. 힌트가 있을 때만 hint 키를 포함합니다."""
        data: dict = {
            "question": self.question,
            "choices": list(self.choices),
            "answer": self.answer,
        }
        if self.has_hint():
            data["hint"] = self.hint
        return data

    @classmethod
    def from_dict(cls, data : dict) -> 'Quiz':
        """state.json에서 읽은 dict로 Quiz 객체를 복원합니다."""
        # cls(...)는 Quiz 생성자를 호출하며, 생성 시 값 검증도 함께 수행됩니다.
        # hint는 선택 항목이므로 get()으로 읽습니다. 키가 없으면 None이 됩니다.
        return cls(data["question"], data["choices"], data["answer"], data.get("hint"))