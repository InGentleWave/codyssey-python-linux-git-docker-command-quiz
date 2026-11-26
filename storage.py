"""state.json 파일의 저장과 불러오기, 데이터 검증, 백업을 담당합니다."""

import json
import shutil
from pathlib import Path

from default_quizzes import get_builtin_quizzes, read_default_data
from quiz import Quiz

# 데이터 파일 경로입니다. __file__은 이 파일의 경로이고, parent는 그 파일이 있는 폴더(프로젝트 루트)입니다.
STATE_PATH: Path = Path(__file__).resolve().parent / "state.json"
# 저장 직전의 state.json을 복사해 두는 백업 파일입니다. state.json이 손상되면 이 파일로 복구합니다.
BACKUP_PATH: Path = STATE_PATH.with_name("state.json.bak")
# 손상된 state.json을 덮어쓰기 전에 옮겨 두는 파일입니다. 사용자가 직접 내용을 확인할 수 있습니다.
BROKEN_PATH: Path = STATE_PATH.with_name("state.json.broken")

# 불러온 상태의 형태: (퀴즈 목록, 최고 점수, 게임 기록 목록)
State = tuple[list[Quiz], int | None, list[dict]]

# 파일 읽기 실패, JSON 형식 오류, 키 누락, 값 오류를 모두 같은 방식으로 처리하기 위한 예외 묶음입니다.
# UnicodeDecodeError는 ValueError의 하위 클래스이므로 여기서 함께 잡힙니다.
LOAD_ERRORS: tuple[type[Exception], ...] = (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError)


# history 항목 하나가 가져야 하는 키와 자료형입니다.
HISTORY_FIELDS: dict[str, type] = {
    "played_at": str,
    "questions_solved": int,
    "correct_count": int,
    "score": int,
    "hints_used": int,
}


def is_plain_int(value: object) -> bool:
    """bool이 아닌 정수이면 True를 반환합니다.
    bool은 int의 하위 클래스이므로 isinstance(True, int)가 True가 됩니다. 이를 막기 위해 bool을 따로 제외합니다."""
    return isinstance(value, int) and not isinstance(value, bool)


def validate_record(record: object) -> None:
    """history 항목 하나를 검사합니다. 잘못되었으면 ValueError를 발생시킵니다."""
    if not isinstance(record, dict):
        raise ValueError("기록 항목이 객체가 아닙니다.")
    for key, expected_type in HISTORY_FIELDS.items():
        value: object = record.get(key)
        valid: bool = is_plain_int(value) if expected_type is int else isinstance(value, expected_type)
        if not valid:
            raise ValueError(f"기록 항목의 {key} 값이 잘못되었습니다.")
    if not 0 <= record["score"] <= 100:
        raise ValueError("기록 항목의 점수 값이 잘못되었습니다.")


def validate_state(data: object) -> State:
    """JSON에서 읽은 값을 검사하고 (퀴즈 목록, 최고 점수, 기록 목록)으로 변환합니다.
    state.json과 default_quizzes.json이 같은 구조이므로 두 파일 모두 이 함수로 검증합니다.
    값이 잘못되었으면 ValueError(또는 KeyError, TypeError)를 발생시킵니다."""
    # 최상위 값이 객체(dict)가 아니면 잘못된 데이터입니다.
    if not isinstance(data, dict):
        raise ValueError("최상위 값이 객체가 아닙니다.")

    # 각 항목을 Quiz 객체로 복원합니다. 값이 잘못되면 Quiz 생성자가 ValueError를 발생시킵니다.
    quizzes: list[Quiz] = [Quiz.from_dict(item) for item in data["quizzes"]]
    best_score: int | None = data["best_score"]
    history: list[dict] = data["history"]

    # 최고 점수는 None(미풀이) 또는 0~100 사이의 정수여야 합니다.
    if best_score is not None and (not is_plain_int(best_score) or not 0 <= best_score <= 100):
        raise ValueError("최고 점수 값이 잘못되었습니다.")
    if not isinstance(history, list):
        raise ValueError("기록의 형식이 잘못되었습니다.")
    for record in history:
        validate_record(record)

    return quizzes, best_score, history


def load_default_state() -> State:
    """default_quizzes.json으로 기본 상태를 만듭니다.
    이 파일도 읽을 수 없으면 코드에 내장된 기본 퀴즈로 시작합니다."""
    try:
        return validate_state(read_default_data())
    except LOAD_ERRORS:
        print("default_quizzes.json 파일을 읽을 수 없어 내장 기본 퀴즈로 시작합니다.")
        # 내장 퀴즈, 최고 점수 없음(None), 빈 기록으로 시작합니다.
        return get_builtin_quizzes(), None, []


def read_state_file(path: Path) -> State:
    """state.json 형식의 파일을 읽고 검증해 반환합니다. 실패하면 LOAD_ERRORS 중 하나가 발생합니다."""
    with path.open("r", encoding="utf-8") as file:
        # JSON 텍스트를 dict로 변환합니다. 형식이 잘못되면 JSONDecodeError가 발생합니다.
        data: object = json.load(file)
    return validate_state(data)


def keep_broken_file() -> None:
    """손상된 state.json을 state.json.broken으로 옮겨, 다음 저장 때 덮어써 사라지지 않게 합니다."""
    try:
        # replace는 같은 이름의 파일이 있으면 덮어씁니다(가장 최근 손상본만 보관).
        STATE_PATH.replace(BROKEN_PATH)
        print(f"손상된 파일은 {BROKEN_PATH.name}으로 옮겨 두었습니다.")
    except OSError as error:
        print(f"손상된 파일을 옮기지 못했습니다: {error}")


def load_state() -> State:
    """(퀴즈 목록, 최고 점수, 기록 목록)을 불러옵니다.
    읽는 순서: state.json → state.json.bak → default_quizzes.json → 코드 내장 퀴즈"""
    # 파일이 없으면 첫 실행으로 보고 기본 데이터를 사용합니다.
    if not STATE_PATH.exists():
        print("저장된 데이터가 없어 기본 퀴즈로 시작합니다.")
        return load_default_state()

    try:
        state: State = read_state_file(STATE_PATH)
    except LOAD_ERRORS:
        print("state.json 파일을 읽을 수 없습니다.")
        keep_broken_file()
    else:
        print("저장된 데이터를 불러왔습니다.")
        return state

    # state.json이 손상되었으면 마지막 백업으로 복구를 시도합니다.
    if BACKUP_PATH.exists():
        try:
            state = read_state_file(BACKUP_PATH)
        except LOAD_ERRORS:
            print(f"{BACKUP_PATH.name}도 읽을 수 없습니다.")
        else:
            print(f"{BACKUP_PATH.name}(마지막 저장 직전의 백업)에서 데이터를 복구했습니다.")
            return state

    print("기본 퀴즈로 시작합니다.")
    return load_default_state()


def backup_state() -> None:
    """저장하기 직전에 기존 state.json을 state.json.bak으로 복사합니다."""
    if not STATE_PATH.exists():
        return
    try:
        # copy2는 내용과 함께 수정 시각 같은 파일 정보도 복사합니다.
        shutil.copy2(STATE_PATH, BACKUP_PATH)
    except OSError as error:
        # 백업에 실패해도 저장은 계속 진행합니다.
        print(f"백업 파일을 만들지 못했습니다: {error}")


def save_state(quizzes: list[Quiz], best_score: int | None, history: list[dict]) -> None:
    """퀴즈 목록, 최고 점수, 기록을 state.json에 UTF-8로 저장합니다."""
    # 설계 5절의 스키마에 맞춰 dict를 만듭니다.
    data: dict = {
        "quizzes": [quiz.to_dict() for quiz in quizzes],
        "best_score": best_score,
        "history": history,
    }

    # "w" 모드로 여는 순간 기존 내용이 지워지므로, 먼저 백업합니다.
    backup_state()

    try:
        with STATE_PATH.open("w", encoding="utf-8") as file:
            # ensure_ascii=False: 한글을 \uXXXX 형태로 바꾸지 않고 그대로 저장합니다.
            # indent=2: 사람이 읽기 쉽도록 들여쓰기를 줍니다.
            json.dump(data, file, ensure_ascii=False, indent=2)
    except OSError as error:
        # 쓰기 실패 시 프로그램이 멈추지 않도록 안내만 출력합니다.
        print(f"데이터를 저장하지 못했습니다: {error}")
