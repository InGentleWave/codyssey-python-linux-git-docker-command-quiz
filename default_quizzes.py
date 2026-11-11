"""기본 퀴즈 데이터. 첫 실행 또는 state.json 복구 시 사용합니다."""

# Quiz 클래스를 가져옵니다.
from quiz import Quiz


def get_default_quizzes():
    """Git, Docker, Linux 주제의 기본 Quiz 목록을 반환합니다."""
    # 각 Quiz는 (문제, 선택지 4개 리스트, 정답 번호 1~4) 순서로 만듭니다.
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