"""state.json 파일의 저장과 불러오기를 담당합니다."""

import json
from pathlib import Path

from default_quizzes import get_default_quizzes
from quiz import Quiz

# 데이터 파일 경로입니다. __file__은 이 파일의 경로이고, parent는 그 파일이 있는 폴더(프로젝트 루트)입니다.
STATE_PATH: Path = Path(__file__).resolve().parent / "state.json"


def load_state() -> tuple[list[Quiz], int | None, list[dict]]:
    """state.json에서 (퀴즈 목록, 최고 점수, 기록 목록)을 읽어 반환합니다.
    파일이 없거나 손상되었으면 안내 후 기본 데이터를 반환합니다."""
    # 기본 데이터: 기본 퀴즈, 최고 점수 없음(None), 빈 기록 (설계 5절)
    default_state: tuple[list[Quiz], int | None, list[dict]] = (get_default_quizzes(), None, [])

    # 파일이 없으면 첫 실행으로 보고 기본 데이터를 사용합니다.
    if not STATE_PATH.exists():
        print("저장된 데이터가 없어 기본 퀴즈로 시작합니다.")
        return default_state

    try:
        with STATE_PATH.open("r", encoding="utf-8") as file:
            # JSON 텍스트를 dict로 변환합니다. 형식이 잘못되면 JSONDecodeError가 발생합니다.
            data = json.load(file)

        # 최상위 값이 객체(dict)가 아니면 잘못된 데이터입니다.
        if not isinstance(data, dict):
            raise ValueError("최상위 값이 객체가 아닙니다.")

        # 각 항목을 Quiz 객체로 복원합니다. 값이 잘못되면 Quiz 생성자가 ValueError를 발생시킵니다.
        quizzes: list[Quiz] = [Quiz.from_dict(item) for item in data["quizzes"]]
        best_score: int = data["best_score"]
        history: list[dict] = data["history"]

        # 최고 점수는 None(미풀이) 또는 0~100 사이의 정수여야 합니다.
        # bool은 int의 하위 클래스이므로 isinstance(True, int)가 True가 됩니다. 이를 막기 위해 bool을 따로 제외합니다.
        if best_score is not None and (
            isinstance(best_score, bool)
            or not isinstance(best_score, int)
            or not 0 <= best_score <= 100
        ):
            raise ValueError("최고 점수 값이 잘못되었습니다.")
        if not isinstance(history, list):
            raise ValueError("기록의 형식이 잘못되었습니다.")

    except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError):
        # 읽기 실패, JSON 형식 오류, 키 누락, 값 오류를 모두 같은 방식으로 처리합니다.
        # UnicodeDecodeError는 ValueError의 하위 클래스이므로 여기서 함께 잡힙니다.
        print("state.json 파일을 읽을 수 없어 기본 퀴즈로 시작합니다.")
        return default_state

    print("저장된 데이터를 불러왔습니다.")
    return quizzes, best_score, history


def save_state(quizzes: list[Quiz], best_score: int | None, history: list[dict]) -> None:
    """퀴즈 목록, 최고 점수, 기록을 state.json에 UTF-8로 저장합니다."""
    # 설계 5절의 스키마에 맞춰 dict를 만듭니다.
    data: dict = {
        "quizzes": [quiz.to_dict() for quiz in quizzes],
        "best_score": best_score,
        "history": history,
    }

    try:
        with STATE_PATH.open("w", encoding="utf-8") as file:
            # ensure_ascii=False: 한글을 \uXXXX 형태로 바꾸지 않고 그대로 저장합니다.
            # indent=2: 사람이 읽기 쉽도록 들여쓰기를 줍니다.
            json.dump(data, file, ensure_ascii=False, indent=2)
    except OSError as error:
        # 쓰기 실패 시 프로그램이 멈추지 않도록 안내만 출력합니다.
        print(f"데이터를 저장하지 못했습니다: {error}")