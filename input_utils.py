"""공통 입력 검증 함수 모음."""


def ask_int(prompt, min_value, max_value):
    """정수 입력을 받아 범위 안의 값을 반환합니다. 잘못된 입력은 다시 묻습니다."""
    # 올바른 값을 받을 때까지 반복합니다.
    while True:
        # input()으로 입력을 받고, strip()으로 앞뒤 공백을 제거합니다.
        raw = input(prompt).strip()

        # 빈 입력이면 안내 후 다시 입력받습니다.
        if raw == "":
            print("입력값이 비어 있습니다. 다시 입력해 주세요.")
            continue

        # 숫자로 변환할 수 없는 값(예: abc)은 ValueError가 발생하므로 잡아서 처리합니다.
        try:
            value = int(raw)
        except ValueError:
            print("숫자만 입력해 주세요.")
            continue

        # 허용 범위 밖의 숫자(예: 메뉴 9)는 안내 후 다시 입력받습니다.
        if value < min_value or value > max_value:
            print(f"{min_value}부터 {max_value} 사이의 숫자를 입력해 주세요.")
            continue

        # 모든 검사를 통과한 값만 반환합니다.
        return value

def ask_text(prompt: str) -> str:
    """빈 입력이 아닌 텍스트를 받을 때까지 다시 묻고, 앞뒤 공백을 제거해 반환합니다."""
    while True:
        # 입력을 받고 앞뒤 공백을 제거합니다.
        raw: str = input(prompt).strip()

        # 공백만 입력했거나 아무것도 입력하지 않은 경우 다시 입력받습니다.
        if raw == "":
            print("입력값이 비어 있습니다. 다시 입력해 주세요.")
            continue

        # 검사를 통과한 문자열만 반환합니다.
        return raw