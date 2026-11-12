"""기본 퀴즈 데이터. 첫 실행 또는 state.json 복구 시 사용합니다."""
import json
from pathlib import Path

# Quiz 클래스를 가져옵니다.
from quiz import Quiz

# 데이터 파일 경로입니다. __file__은 이 파일의 경로이고, parent는 그 파일이 있는 폴더(프로젝트 루트)입니다.
DEFAULT_QUIZZES_PATH: Path = Path(__file__).resolve().parent / "default_quizzes.json"

def get_default_quizzes():
    """Git, Docker, Linux 주제의 기본 Quiz 목록을 반환합니다."""
    # 각 Quiz는 (문제, 선택지 4개 리스트, 정답 번호 1~4) 순서로 만듭니다.
    try:
        with DEFAULT_QUIZZES_PATH.open("r", encoding="utf-8") as file:
            # JSON 텍스트를 dict로 변환합니다. 형식이 잘못되면 JSONDecodeError가 발생합니다.
            data = json.load(file)

        # 최상위 값이 객체(dict)가 아니면 잘못된 데이터입니다.
        if not isinstance(data, dict):
            raise ValueError("최상위 값이 객체가 아닙니다.")

        # 각 항목을 Quiz 객체로 복원합니다. 값이 잘못되면 Quiz 생성자가 ValueError를 발생시킵니다.
        quizzes: list[Quiz] = [Quiz.from_dict(item) for item in data["quizzes"]]
        best_score: int | None = data["best_score"]
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

        return quizzes, best_score, history
    except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError):
        # 읽기 실패, JSON 형식 오류, 키 누락, 값 오류를 모두 같은 방식으로 처리합니다.
        # UnicodeDecodeError는 ValueError의 하위 클래스이므로 여기서 함께 잡힙니다.
        print("default_quizzes.json 파일을 읽을 수 없어 기본 퀴즈로 시작합니다.")
        return [
            Quiz(
                "변경 사항을 스테이징 영역에 올리는 Git 명령어는?",
                ["git commit", "git add", "git push", "git clone"],
                2,  # 정답: git add (2번)
            ),
            Quiz(
                "새 브랜치를 만들고 바로 전환하는 Git 명령어는?",
                ["git branch -d", "git checkout -b", "git merge", "git pull"],
                2,  # 정답: git checkout -b (-b 옵션이 브랜치 생성을 의미)
            ),
            Quiz(
                "실행 중인 Docker 컨테이너 목록을 확인하는 명령어는?",
                ["docker images", "docker ps", "docker build", "docker pull"],
                2,  # 정답: docker ps (실행 중인 컨테이너 목록 출력)
            ),
            Quiz(
                "이미지로 컨테이너를 만들고 실행하는 Docker 명령어는?",
                ["docker run", "docker save", "docker tag", "docker rmi"],
                1,  # 정답: docker run
            ),
            Quiz(
                "현재 작업 디렉터리의 경로를 출력하는 Linux 명령어는?",
                ["ls", "pwd", "cd", "mkdir"],
                2,  # 정답: pwd (print working directory)
            ),
            Quiz(
                "파일의 내용을 화면에 출력하는 Linux 명령어는?",
                ["cat", "rm", "cp", "mv"],
                1,  # 정답: cat
            ),
        ]