"""기본 퀴즈 데이터. 첫 실행 또는 state.json 복구 시 사용합니다."""
import json
from pathlib import Path

# Quiz 클래스를 가져옵니다.
from quiz import Quiz

# 데이터 파일 경로입니다. __file__은 이 파일의 경로이고, parent는 그 파일이 있는 폴더(프로젝트 루트)입니다.
DEFAULT_QUIZZES_PATH: Path = Path(__file__).resolve().parent / "default_quizzes.json"


def read_default_data() -> dict:
    """default_quizzes.json을 읽어 dict로 반환합니다.
    읽기 오류와 형식 오류는 호출한 쪽(storage.py)에서 검증하고 처리합니다."""
    with DEFAULT_QUIZZES_PATH.open("r", encoding="utf-8") as file:
        # JSON 텍스트를 dict로 변환합니다. 형식이 잘못되면 JSONDecodeError가 발생합니다.
        return json.load(file)


def get_builtin_quizzes() -> list[Quiz]:
    """default_quizzes.json도 읽을 수 없을 때 사용하는, 코드에 내장된 기본 퀴즈 6개를 반환합니다."""
    # 각 Quiz는 (문제, 선택지 4개 리스트, 정답 번호 1~4, 힌트) 순서로 만듭니다.
    return [
        Quiz(
            "변경 사항을 스테이징 영역에 올리는 Git 명령어는?",
            ["git commit", "git add", "git push", "git clone"],
            2,  # 정답: git add (2번)
            "'추가하다'라는 뜻의 영어 단어입니다.",
        ),
        Quiz(
            "새 브랜치를 만들고 바로 전환하는 Git 명령어는?",
            ["git branch -d", "git checkout -b", "git merge", "git pull"],
            2,  # 정답: git checkout -b (-b 옵션이 브랜치 생성을 의미)
            "-b 옵션은 branch의 첫 글자입니다.",
        ),
        Quiz(
            "실행 중인 Docker 컨테이너 목록을 확인하는 명령어는?",
            ["docker images", "docker ps", "docker build", "docker pull"],
            2,  # 정답: docker ps (실행 중인 컨테이너 목록 출력)
            "Linux에서 실행 중인 프로세스를 보는 명령어와 이름이 같습니다.",
        ),
        Quiz(
            "이미지로 컨테이너를 만들고 실행하는 Docker 명령어는?",
            ["docker run", "docker save", "docker tag", "docker rmi"],
            1,  # 정답: docker run
            "'실행하다'라는 뜻의 영어 단어입니다.",
        ),
        Quiz(
            "현재 작업 디렉터리의 경로를 출력하는 Linux 명령어는?",
            ["ls", "pwd", "cd", "mkdir"],
            2,  # 정답: pwd (print working directory)
            "print working directory의 약자입니다.",
        ),
        Quiz(
            "파일의 내용을 화면에 출력하는 Linux 명령어는?",
            ["cat", "rm", "cp", "mv"],
            1,  # 정답: cat
            "concatenate(이어 붙이다)의 줄임말입니다.",
        ),
    ]
