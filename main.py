"""퀴즈 게임 실행 진입점."""

# 숫자 입력을 검증하는 함수를 가져옵니다.
from input_utils import ask_int

# 메뉴 항목 목록입니다. 순서대로 1번, 2번, ... 이 됩니다.
MENU_ITEMS = [
    "퀴즈 풀기",
    "퀴즈 추가",
    "퀴즈 목록",
    "점수 확인",
    "종료",
]
# 마지막 항목(종료)의 번호입니다. 항목 개수가 바뀌어도 자동으로 맞춰집니다.
EXIT_NUMBER = len(MENU_ITEMS)


def show_menu():
    """메뉴 목록을 출력합니다."""
    print("\n=== 나만의 퀴즈 게임 ===")
    # enumerate의 start=1로 메뉴 번호를 1부터 붙여 출력합니다.
    for number, label in enumerate(MENU_ITEMS, start=1):
        print(f"{number}. {label}")


def run():
    """메뉴를 반복 출력하고 선택된 번호를 처리합니다."""
    # 종료를 선택할 때까지 메뉴를 계속 보여줍니다.
    while True:
        show_menu()
        # 1 ~ EXIT_NUMBER 범위의 정수만 받도록 검증합니다.
        choice = ask_int("메뉴 번호를 입력하세요: ", 1, EXIT_NUMBER)

        # 종료를 선택하면 반복을 빠져나와 프로그램을 끝냅니다.
        if choice == EXIT_NUMBER:
            print("프로그램을 종료합니다.")
            break

        # 1~4번 기능은 설계 8.2의 #6~9에서 구현할 예정이므로 안내 문구만 출력합니다.
        print("이 메뉴는 아직 구현되지 않았습니다.")


# 이 파일을 직접 실행했을 때만 아래 코드가 동작합니다 (다른 파일에서 import하면 실행되지 않음).
if __name__ == "__main__":
    try:
        run()
    except Exception as error:
        # 예상하지 못한 오류가 나면 내용을 출력합니다.
        print(f"오류가 발생했습니다: {error}")
        # 바로 창이 닫히지 않도록 Enter 입력을 기다린 뒤 종료합니다.
        input("Enter를 누르면 종료합니다...")