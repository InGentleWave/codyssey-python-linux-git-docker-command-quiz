# 나만의 퀴즈 게임

## 프로젝트 개요

- **나만의 퀴즈 게임**은 터미널에서 실행하는 Python 콘솔 퀴즈 프로그램입니다.
- 사용자는 자신의 주제로 만든 4지선다 퀴즈를 직접 추가하고, 퀴즈를 풀고, 최고 점수를 확인할 수 있습니다.
- 프로그램을 종료하고 다시 실행해도 추가한 퀴즈와 최고 점수가 유지됩니다.
- 기본 주제는 Git, Docker, Linux 명령어 입니다.

### 목표

- 메뉴에서 번호를 선택해 퀴즈 풀기, 퀴즈 추가, 퀴즈 목록, 퀴즈 삭제, 점수 확인, 종료를 사용할 수 있다.
- 입력/출력 흐름, 클래스(Quiz, QuizSession, QuizGame), 파일 입출력(JSON)을 하나의 프로그램에 적용한다.
- 퀴즈와 최고 점수를 `state.json`(UTF-8)에 저장해 데이터가 유지되게 한다.
- 기능 단위 커밋, 브랜치 생성과 병합, clone과 pull로 Git 이력을 관리하고 GitHub에 공개한다.

### 대상 사용자

자신의 주제에 맞는 지식을 퀴즈로 학습하려는 학습자입니다.

### 범위

- 포함: 기본 5가지 메뉴 기능, 주제 퀴즈 5개 이상(문제, 선택지 4개, 정답), 잘못된 입력과 데이터 파일 오류 처리
- 포함(보너스): 랜덤 출제, 문제 수 선택, 힌트(힌트를 쓴 문제는 정답이어도 0.5문제로 계산), 퀴즈 삭제, 모든 게임 기록 저장
- 제약: Python 3.10 이상, 외부 라이브러리 없이 표준 라이브러리만 사용

### 완료 기준

- 종료 후 재실행해도 추가한 퀴즈와 최고 점수가 유지된다.
- 클래스가 2개 이상이고 기능별로 메서드가 분리되어 있다.
- 커밋이 10개 이상이고 브랜치 병합, clone, pull 기록이 있다.
- README에 필수 항목 6개가 포함되어 있다.

### 산출물

Python 콘솔 프로그램 1개와 GitHub 저장소 1개입니다. 제출물은 저장소 URL, 개발 환경 스크린샷, 실행 결과 스크린샷, `git log --oneline --graph` 스크린샷입니다.

## 퀴즈 주제 선정 이유

- 주제: Git, Docker, Linux 명령어
- 선정 이유: 팀 개발에서 자주 쓰이지만 아직 익숙하지 않은 명령어를 더 빨리 익히고 싶었습니다. 이 프로젝트를 수행한 결과물을 추후 학습에 활용할 계획입니다.

## 실행 방법

### 사전 준비

- Python 3.10 이상이 필요합니다(개발 환경: Python 3.14). 외부 라이브러리는 사용하지 않습니다.
- 저장소를 내려받습니다.

```bash
git clone https://github.com/InGentleWave/codyssey-python-linux-git-docker-command-quiz.git
cd codyssey-python-linux-git-docker-command-quiz
```

### 1. 기본 주제(Git, Docker, Linux 명령어)로 실행

파일을 수정하지 않고 아래 명령어로 실행합니다.

```bash
python3 main.py
```

Windows PowerShell에서는 `python main.py`로 실행합니다.

1. 메뉴에서 1번(퀴즈 풀기)을 선택합니다.
2. 풀이 모드를 선택합니다: 기본, 랜덤, 기본+힌트, 랜덤+힌트
3. 풀 문제 수를 입력합니다(1 ~ 저장된 퀴즈 수).
4. 보기 번호(1~4)를 입력해 답합니다. 힌트 모드에서는 0을 입력하면 힌트를 볼 수 있습니다.

### 2. 나만의 주제로 기본 퀴즈 파일 설정 후 시작하기

기본 퀴즈 파일의 내용을 원하는 주제의 문제로 바꾸면 같은 방법으로 실행할 수 있습니다.

#### default_quizzes.json 변경 방법

1. 프로그램을 종료한 상태에서 `default_quizzes.json`을 엽니다.
2. 문제 항목을 아래 형식에 맞게 수정하거나 추가합니다.

```json
{
  "question": "문제 내용",
  "choices": ["보기1", "보기2", "보기3", "보기4"],
  "answer": 1,
  "hint": "힌트 내용(선택)"
}
```

3. 항목 작성 규칙
   - `choices`는 보기 4개를 문자열로 적습니다.
   - `answer`는 정답 보기 번호(1~4)입니다.
   - `hint`는 생략할 수 있습니다.
   - 파일은 UTF-8로 저장하고, 항목 사이에 쉼표를 빠뜨리지 않습니다.
4. `default_quizzes.json`은 `state.json`이 없을 때만 읽습니다. 바꾼 문제로 시작하려면 `state.json`을 삭제한 뒤 `python3 main.py`로 실행합니다(아래 [백업과 초기화](#백업과-초기화) 참고).

> 프로그램 안의 퀴즈 추가 메뉴로도 문제를 추가할 수 있습니다. 파일을 직접 수정하는 방법은 문제를 한꺼번에 바꿀 때 사용합니다.

## 실행 결과

아래는 실제 실행 화면을 텍스트로 옮긴 것입니다(사용자 입력은 프롬프트 뒤에 함께 적었습니다).

### 메뉴와 잘못된 입력 처리

```text
저장된 데이터를 불러왔습니다.

=== 나만의 퀴즈 게임 ===
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 퀴즈 삭제
5. 점수 확인
6. 종료
메뉴 번호를 입력하세요: abc
숫자만 입력해 주세요.
메뉴 번호를 입력하세요: 9
1부터 6 사이의 숫자를 입력해 주세요.
메뉴 번호를 입력하세요:
입력값이 비어 있습니다. 다시 입력해 주세요.
```

### 퀴즈 풀기 (랜덤 + 힌트, 3문제)

```text
메뉴 번호를 입력하세요: 1

풀이 모드를 선택하세요. (힌트 모드: 힌트를 본 문제는 맞혀도 0.5점)
1. 기본 (저장된 순서대로 출제)
2. 랜덤 (순서를 섞어 출제)
3. 기본 + 힌트
4. 랜덤 + 힌트
모드 번호를 입력하세요: 4
풀 문제 수를 입력하세요 (1~6): 3

[랜덤 + 힌트] 3문제를 시작합니다.

[1/3]
변경 사항을 스테이징 영역에 올리는 Git 명령어는?
  1. git commit
  2. git add
  3. git push
  4. git clone
정답 번호를 입력하세요 (힌트 보기: 0): 0
힌트: '추가하다'라는 뜻의 영어 단어입니다. (이 문제는 맞혀도 0.5점입니다)
정답 번호를 입력하세요 (힌트 보기: 0): 2
정답입니다.
... (중략) ...

결과: 3문제 중 3문제 정답 (점수: 83점), 사용한 힌트 1개
최고 점수를 갱신했습니다.
```

### 퀴즈 추가

```text
메뉴 번호를 입력하세요: 2
문제를 입력하세요: 영화 '기생충'의 감독은?
선택지 1번: 박찬욱
선택지 2번: 봉준호
선택지 3번: 김기덕
선택지 4번: 이창동
정답 번호를 입력하세요 (1~4): 2
힌트를 입력하세요 (없으면 Enter): 칸 영화제 황금종려상 수상 감독입니다.
퀴즈가 추가되었습니다.
```

### 퀴즈 삭제

```text
메뉴 번호를 입력하세요: 4

등록된 퀴즈 목록 (총 7개)
[1] 변경 사항을 스테이징 영역에 올리는 Git 명령어는?
...
[7] 영화 '기생충'의 감독은?
삭제할 퀴즈 번호를 입력하세요 (취소: 0, 1~7): 7

영화 '기생충'의 감독은?
  1. 박찬욱
  2. 봉준호
  3. 김기덕
  4. 이창동
이 퀴즈를 삭제할까요? (y/n): y
퀴즈를 삭제했습니다.
```

### 점수 확인 (최고 점수 + 게임 기록)

```text
메뉴 번호를 입력하세요: 5
최고 점수: 83점

게임 기록 (총 1회, 최근 1회)
- 2026-11-26 17:48:32 | 3문제 중 3문제 정답 | 83점 | 힌트 1개
```

### 스크린샷

`docs/screenshots/`에 있는 캡처 화면입니다.

| 내용 | 파일 |
|---|---|
| 개발 환경(Python, Git 버전) | [2026-11-10_env-check_code-python-git-version.png](docs/screenshots/2026-11-10_env-check_code-python-git-version.png) |
| 퀴즈 풀기 | [2026-11-11_quiz_playing.png](docs/screenshots/2026-11-11_quiz_playing.png) |
| 퀴즈 추가 | [2026-11-12_add_quiz.png](docs/screenshots/2026-11-12_add_quiz.png) |
| 퀴즈 목록 | [2026-11-12_quiz_list.png](docs/screenshots/2026-11-12_quiz_list.png) |
| 점수 확인 | [2026-11-12_quiz_best_score.png](docs/screenshots/2026-11-12_quiz_best_score.png) |
| `git log --oneline --graph` | [2026-11-12_git_log_oneline_graph.png](docs/screenshots/2026-11-12_git_log_oneline_graph.png) |

## 기능 목록

### 기본 기능

| 번호 | 기능 | 설명 |
|---|---|---|
| 1 | 퀴즈 풀기 | 모드와 문제 수를 고른 뒤 퀴즈를 출제하고, 정답을 채점해 결과를 출력합니다. |
| 2 | 퀴즈 추가 | 문제, 선택지 4개, 정답 번호, 힌트(선택)를 입력해 새 퀴즈를 등록합니다. |
| 3 | 퀴즈 목록 | 저장된 퀴즈를 정답, 힌트와 함께 출력합니다. 퀴즈가 없으면 안내 메시지를 출력합니다. |
| 4 | 퀴즈 삭제 | 번호로 퀴즈를 골라 y/n 확인 후 삭제합니다. 0을 입력하면 취소합니다. (보너스) |
| 5 | 점수 확인 | 최고 점수와 최근 게임 기록 5회를 출력합니다. 아직 풀지 않았으면 안내 메시지를 출력합니다. |
| 6 | 종료 | 데이터를 저장하고 프로그램을 종료합니다. |

### 공통 기능

- 입력 검증: 앞뒤 공백을 제거하고, 문자 입력, 범위 밖 숫자, 빈 입력은 안내 후 다시 입력받습니다.
- 안전한 종료: Ctrl+C와 EOF 입력 시 안내 메시지를 출력하고 가능한 범위에서 저장한 뒤 종료합니다.
- 기본 퀴즈 제공: Git, Docker, Linux 명령어 퀴즈 6개(힌트 포함)를 기본으로 제공합니다.
- 데이터 저장: 퀴즈와 최고 점수, 게임 기록을 `state.json`에 UTF-8로 저장하고, 재실행 시 불러옵니다.
- 오류 대응: 데이터 파일이 없으면 기본 데이터로 시작하고, 손상되었으면 손상 파일을 보존한 뒤 백업이나 기본 데이터로 복구합니다.

### 보너스 기능

| 기능 | 설명 |
|---|---|
| 퀴즈 모드 선택 | 퀴즈를 시작할 때 기본, 랜덤, 기본+힌트, 랜덤+힌트 중 하나를 선택합니다. |
| 랜덤 출제 | 랜덤 모드에서는 `random.sample`로 원본 순서를 유지한 채 무작위로 뽑아 출제합니다. |
| 문제 수 선택 | 풀 문제 수를 직접 입력합니다. 0개나 전체 퀴즈 수 초과는 다시 입력받습니다. |
| 힌트 | 힌트 모드에서 0을 입력하면 힌트를 봅니다. 힌트를 사용한 문제는 정답이어도 0.5점으로 계산하며, 결과에는 사용한 힌트 개수를 표시합니다. |
| 퀴즈 삭제 | 등록된 퀴즈를 삭제하고 바로 파일에 반영합니다. |
| 게임 기록 저장 | 게임이 끝날 때마다 날짜와 시간, 푼 문제 수, 정답 수, 점수, 힌트 사용 수를 `state.json`에 저장합니다. |

## 파일 구조

```text
codyssey-python-linux-git-docker-command-quiz/
├── docs/
│   ├── screenshots/        # 제출용 캡처 화면
│   └── command-log.md      # Git 명령어 사용 기록
├── .gitignore
├── README.md
├── main.py                 # 실행 진입점, Ctrl+C/EOF 처리
├── quiz.py                 # Quiz 클래스: 퀴즈 한 문항
├── quiz_session.py         # QuizSession 클래스: 한 판의 출제와 채점
├── quiz_game.py            # QuizGame 클래스: 메뉴와 게임 상태 관리
├── input_utils.py          # 공통 입력 검증 함수
├── storage.py              # state.json 읽기/쓰기, 검증, 백업
├── default_quizzes.py      # 기본 퀴즈 파일 읽기, 코드 내장 퀴즈
├── default_quizzes.json    # 기본 퀴즈 데이터
└── state.json              # 실행 중 변경되는 데이터(퀴즈, 최고 점수, 기록)
```

실행 중에는 `state.json.bak`(백업)과 `state.json.broken`(손상 파일 보관본)이 만들어질 수 있습니다. 두 파일은 `.gitignore`로 저장소에서 제외합니다.

## 설계

### 클래스 구조

| 클래스 | 파일 | 책임 |
|---|---|---|
| `Quiz` | quiz.py | 퀴즈 한 문항의 데이터(문제, 선택지, 정답, 힌트)를 가지고, 생성 시 값을 검증하며, 출력과 정답 확인, dict 변환을 담당합니다. |
| `QuizSession` | quiz_session.py | 퀴즈 한 판을 담당합니다. 출제할 문제를 고르고(순서, 개수), 답과 힌트 요청을 받아 채점한 뒤 게임 기록을 만듭니다. |
| `QuizGame` | quiz_game.py | 프로그램 전체 상태(퀴즈 목록, 최고 점수, 기록)를 가지고 메뉴를 실행하며, 변경 사항을 저장합니다. |

### 클래스를 사용한 이유

- **데이터와 동작을 함께 묶습니다.** 퀴즈 하나는 문제, 선택지, 정답이 항상 함께 다녀야 합니다. `Quiz` 객체로 묶으면 `quiz.check_answer(2)`처럼 데이터와 그 데이터를 다루는 동작을 한곳에서 관리할 수 있습니다. 함수와 dict만 쓰면 `check_answer(quiz_dict, 2)`처럼 데이터를 매번 넘겨야 하고, 키 이름을 틀려도 실행해 보기 전까지 알기 어렵습니다.
- **잘못된 데이터가 들어오지 못하게 합니다.** `Quiz.__init__`이 선택지 개수와 정답 범위를 검사하므로, 퀴즈 추가 메뉴로 만들든 파일에서 읽든 같은 규칙이 적용됩니다.
- **전역 변수 없이 상태를 관리합니다.** 퀴즈 목록과 최고 점수는 여러 메뉴가 함께 읽고 바꿉니다. 함수만 쓰면 전역 변수나 많은 매개변수가 필요하지만, `QuizGame`의 속성(`self.quizzes`, `self.best_score`)으로 두면 메서드들이 같은 상태를 자연스럽게 공유합니다.
- **기능을 추가해도 영향 범위가 작습니다.** 보너스 기능(모드, 힌트, 기록)은 대부분 `QuizSession` 안에서 끝나므로, 메뉴를 담당하는 `QuizGame`은 거의 바뀌지 않았습니다.

### 모듈 책임 경계

| 모듈 | 하는 일 | 하지 않는 일 |
|---|---|---|
| input_utils.py | 사용자 입력을 받고 형식을 검증 | 게임 규칙 판단 |
| storage.py | 파일 읽기/쓰기, JSON 구조 검증, 백업과 복구 | 화면 메뉴, 채점 |
| default_quizzes.py | 기본 퀴즈 파일 읽기, 내장 퀴즈 제공 | 데이터 검증(storage.py가 담당) |
| quiz_session.py | 한 판의 출제와 채점 | 파일 저장, 최고 점수 관리 |
| quiz_game.py | 메뉴 흐름, 상태 보관, 저장 시점 결정 | 입력 형식 검증, 파일 형식 처리 |

## 데이터 파일 설명

프로젝트 루트에 JSON 파일 2개가 있으며 두 파일의 구조는 같습니다. 모두 UTF-8로 저장합니다.

| 파일 | 경로 | 역할 |
|---|---|---|
| `default_quizzes.json` | 프로젝트 루트 | 기본 퀴즈 데이터입니다. 첫 실행이나 `state.json` 복구 시에 읽습니다. 프로그램이 수정하지 않습니다. |
| `state.json` | 프로젝트 루트 | 실행 중 변경되는 퀴즈 목록, 최고 점수, 게임 기록을 저장합니다. 시작 시 불러오고, 퀴즈 추가/삭제, 게임 종료, 프로그램 종료 시 저장합니다. |

### 파일을 읽을 수 없을 때

데이터는 아래 순서로 불러오며, 앞 단계가 실패하면 다음 단계로 넘어갑니다.

1. `state.json`: 없으면 첫 실행으로 보고 3번으로 갑니다. 손상되었으면 `state.json.broken`으로 옮겨 보존합니다.
2. `state.json.bak`: 마지막 저장 직전의 백업입니다. 정상이면 이 데이터로 복구합니다.
3. `default_quizzes.json`: 기본 퀴즈 데이터로 시작합니다.
4. 코드 내장 퀴즈 6개: `default_quizzes.json`도 읽을 수 없으면 `default_quizzes.py`에 들어 있는 퀴즈로 시작합니다.

### JSON 저장 방식의 한계

- **파일 전체를 매번 다시 씁니다.** 퀴즈 하나만 바뀌어도 `state.json` 전체를 다시 씁니다. 퀴즈와 기록이 수만 개로 늘어나면 저장 시간이 길어집니다.
- **전체를 메모리에 올립니다.** `json.load`는 파일 전체를 한 번에 읽어 메모리에 객체로 만듭니다. 데이터가 커질수록 시작 시간과 메모리 사용량이 함께 늘어납니다.
- **동시 사용을 지원하지 않습니다.** 프로그램 두 개가 동시에 실행되면 나중에 저장한 쪽이 앞의 변경을 덮어씁니다.
- **기록이 계속 쌓입니다.** `history`는 게임마다 늘어나므로 오래 사용하면 파일이 커집니다.
- **대안**: 기록처럼 계속 추가되는 데이터는 한 줄에 객체 하나씩 덧붙이는 NDJSON(JSON Lines)이 적합합니다. 검색, 부분 수정, 동시 접근이 필요하면 표준 라이브러리에 포함된 `sqlite3`(SQLite 데이터베이스)를 사용할 수 있습니다.
- 이 프로젝트는 데이터가 수백 개 수준이고 한 사람이 사용하므로, 사람이 직접 읽고 고칠 수 있는 JSON을 선택했습니다.

### 백업과 초기화

| 상황 | 동작 / 방법 |
|---|---|
| 자동 백업 | 저장할 때마다 기존 `state.json`을 `state.json.bak`으로 복사한 뒤 새로 씁니다. |
| 손상 시 자동 복구 | 손상된 파일은 `state.json.broken`으로 보존하고, `state.json.bak`이 정상이면 백업에서 복구합니다. |
| 수동 복원 | 프로그램을 종료한 뒤 `cp state.json.bak state.json`으로 직전 상태로 되돌립니다. |
| 초기화 | 프로그램을 종료한 뒤 `rm state.json state.json.bak`을 실행하면 다음 실행 때 `default_quizzes.json`으로 새로 시작합니다. |
| 손상 원인 확인 | `state.json.broken`을 열어 어느 부분이 잘못되었는지 확인합니다. |

### state.json, default_quizzes.json 스키마

#### 최상위 구조

| 키 | 타입 | 설명 |
|---|---|---|
| `quizzes` | 배열 | 퀴즈 목록 |
| `best_score` | 정수 또는 null | 최고 점수(0~100). 아직 풀지 않았으면 null입니다. |
| `history` | 배열 | 게임 기록 목록. 처음에는 빈 배열입니다. |

#### quizzes 항목

| 키 | 타입 | 필수 | 설명 |
|---|---|---|---|
| `question` | 문자열 | 필수 | 문제 내용 |
| `choices` | 문자열 배열 | 필수 | 선택지 4개 |
| `answer` | 정수 | 필수 | 정답 번호(1~4) |
| `hint` | 문자열 | 선택 | 힌트 문구. 없으면 해당 문제는 힌트를 사용할 수 없습니다. |

#### history 항목

| 키 | 타입 | 설명 |
|---|---|---|
| `played_at` | 문자열 | 게임을 마친 날짜와 시간(`YYYY-MM-DD HH:MM:SS`) |
| `questions_solved` | 정수 | 푼 문제 수 |
| `correct_count` | 정수 | 맞힌 문제 수 |
| `score` | 정수 | 해당 게임의 점수(0~100) |
| `hints_used` | 정수 | 사용한 힌트 개수 |

#### 예시

퀴즈 하나와 게임 기록 하나가 있는 `state.json`입니다. 퀴즈와 기록은 각각 여러 개가 모이므로 배열로 두고, 항목 하나는 여러 값을 묶은 객체로 두었습니다.

```json
{
  "quizzes": [
    {
      "question": "변경 사항을 스테이징 영역에 올리는 Git 명령어는?",
      "choices": ["git commit", "git add", "git push", "git clone"],
      "answer": 2,
      "hint": "'추가하다'라는 뜻의 영어 단어입니다."
    }
  ],
  "best_score": 83,
  "history": [
    {
      "played_at": "2026-11-26 17:48:32",
      "questions_solved": 3,
      "correct_count": 3,
      "score": 83,
      "hints_used": 1
    }
  ]
}
```

### 점수 계산 규칙

- 점수 = 획득 점수 / 푼 문제 수 x 100을 반올림한 값입니다.
- 정답은 1점, 힌트를 사용해 맞힌 문제는 0.5점, 오답은 0점입니다.
- 예: 3문제를 모두 맞혔지만 1문제에서 힌트를 썼다면 (1 + 1 + 0.5) / 3 x 100 = 83점입니다.
- 게임 점수가 `best_score`보다 높으면 갱신합니다.

## 변경 시 수정 지점

요구사항이 바뀔 때 먼저 확인할 파일과 메서드입니다.

| 바뀌는 요구사항 | 수정할 곳 |
|---|---|
| 메뉴 항목 추가/순서 변경 | quiz_game.py `MENU_ITEMS`, `QuizGame.run`의 번호 분기 |
| 풀이 모드 추가 | quiz_game.py `PLAY_MODES`, quiz_session.py `QuizSession.__init__` |
| 점수 계산 방식 | quiz_session.py `CORRECT_POINT`, `HINT_CORRECT_POINT`, `QuizSession.calculate_score` |
| 힌트 입력 방식(번호 등) | quiz_session.py `HINT_NUMBER`, `QuizSession.ask_answer` |
| 선택지 개수(예: 5지선다) | quiz.py `CHOICE_COUNT`, default_quizzes.json과 `get_builtin_quizzes`의 데이터 |
| 퀴즈 항목에 새 속성 추가 | quiz.py `Quiz.__init__`, `to_dict`, `from_dict` → README 스키마 |
| 게임 기록에 새 값 추가 | quiz_session.py `QuizSession.make_record`, storage.py `HISTORY_FIELDS`, quiz_game.py `show_best_score` |
| 저장 파일 위치나 형식 변경 | storage.py `STATE_PATH`, `read_state_file`, `save_state` |
| 입력 검증 규칙(안내 문구 등) | input_utils.py `ask_int`, `ask_text`, `ask_yes_no` |
| 기본 퀴즈 주제 변경 | default_quizzes.json, default_quizzes.py `get_builtin_quizzes` |
| 최근 기록 표시 개수 | quiz_game.py `RECENT_HISTORY_COUNT` |

## Git 이력 관리

### 커밋 메시지 규칙

- 형식: `접두사: 변경 내용 요약` (요약은 한국어, 한 줄). 필요하면 한 줄을 띄우고 본문에 `-` 목록으로 세부 변경을 적습니다.
- 접두사

| 접두사 | 사용하는 경우 | 예시 |
|---|---|---|
| `Feat` | 새 기능 추가 | `Feat: 퀴즈 삭제 기능 구현` |
| `Fix` | 버그 수정 | `Fix: 비정상 종료처리 수정` |
| `Refactor` | 동작은 그대로 두고 구조만 개선 | `Refactor: QuizGame 책임 분리` |
| `Docs` | README, 주석, 문서 변경 | `Docs: README 실행 방법 추가` |

- 커밋 단위: 동작하는 기능 하나(메뉴, Quiz 클래스, 퀴즈 풀기, 추가, 저장, README 등)를 완성할 때마다 커밋합니다. 서로 관계없는 변경은 한 커밋에 섞지 않습니다.
- 예외: 초기에 GitHub 웹에서 README를 수정한 커밋 2개(`Update README ...`, `Revise README ...`)는 기본 메시지를 그대로 사용했습니다.

### 브랜치 전략

- `main`: 항상 실행 가능한 안정 버전을 유지합니다.
- 작업 브랜치: 기능 하나마다 `main`에서 새 브랜치를 만들어 작업합니다. 이름은 `종류/내용` 형식입니다(예: `feat/hint`, `refactor/structure`, `docs/readme`).
- 브랜치를 나누는 이유: 작업 중인 미완성 코드가 `main`을 깨뜨리지 않게 하고, 기능 단위로 변경 이력을 묶어 보기 위해서입니다.
- 병합 시점: 기능이 완성되고 직접 실행해 확인한 뒤 `main`으로 병합합니다.
- 병합 방식: `git merge --no-ff <브랜치>`를 사용합니다. fast-forward 병합은 브랜치 기록이 일직선으로 합쳐져 어느 커밋이 어느 기능이었는지 보이지 않습니다. `--no-ff`는 병합 커밋을 남겨 `git log --graph`에서 기능 단위로 갈라졌다 합쳐진 흐름이 드러납니다.
- 첫 브랜치 `playQuiz`(퀴즈 풀기 기능)는 fast-forward로 병합되어 병합 커밋이 없습니다. 이후 브랜치는 모두 `--no-ff`로 병합했습니다.

| 브랜치 | 작업 내용 |
|---|---|
| `playQuiz` | 퀴즈 풀기 기능 |
| `refactor/structure` | 검증 로직 통합, QuizSession 분리, fallback 버그 수정 |
| `feat/random-count` | 랜덤 출제, 문제 수 선택 |
| `feat/hint` | 힌트 기능, 기본 퀴즈 힌트 데이터 |
| `feat/delete` | 퀴즈 삭제 |
| `feat/history` | 게임 기록 저장과 조회 |
| `feat/backup` | 자동 백업과 손상 파일 복구 |
| `docs/readme` | README 보강 |

### 원격 저장소와 커밋 이력

- 원격 저장소: https://github.com/InGentleWave/codyssey-python-linux-git-docker-command-quiz
- 커밋 수: `git rev-list --count main`으로 확인합니다. README 보강 시점 기준 46개(병합 커밋 6개 포함)입니다.
- clone, pull, checkout, merge 등 명령어 사용 기록은 [docs/command-log.md](docs/command-log.md)에 있습니다.

`git log --oneline --graph` 결과(보너스 기능 병합 부분):

```text
*   08ad428 Merge branch 'feat/backup'
|\
| * 3eec2b6 Feat: state.json 자동 백업과 손상 파일 복구 구현
|/
*   77ab6e4 Merge branch 'feat/history'
|\
| * d7bc469 Feat: 게임 기록 히스토리 저장과 조회 구현
|/
*   c409653 Merge branch 'feat/delete'
|\
| * e734e97 Feat: 퀴즈 삭제 기능 구현
|/
*   d1764db Merge branch 'feat/hint'
|\
| * f6cc575 Feat: 기본 퀴즈 6개에 힌트 데이터 작성
| * 2e90f6b Feat: 힌트 기능과 힌트 사용 시 점수 차감 구현
|/
*   4fd30dd Merge branch 'feat/random-count'
|\
| * 9a053cf Feat: 랜덤 출제와 문제 수 선택 기능 구현
|/
*   bc89199 Merge branch 'refactor/structure'
|\
| * e0d3885 Refactor: 퀴즈 풀이 로직을 QuizSession으로 분리
| * a514d66 Fix: 기본 데이터 파일 손상 시 내장 퀴즈 반환 형식 오류 수정
|/
* c353f41 Docs: Quiz 선택지 자료형 명시
* 5c621fd Docs: 추가 - /.guide/
...
* 8df735b Initial commit
```
