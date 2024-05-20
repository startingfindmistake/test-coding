# 백준
# 28278번 문제
# 스택 2
# python 언어

# 전체코드
"""
사용자로부터 입력받은 명령에 따라 스택을 조작하고, 각 명령의 결과를 출력하는 역활을 합니다.
"""

# os 모듈을 불러옵니다
import os

# main 함수를 정의합니다
def main():
    # 표준 입력에서 모든 바이트를 읽어와 공백으로 분리하고, 이를 반복 가능한 객체로 만듭니다.
    tokens = iter(os.read(0, os.fstat(0).st_size).split())

    # 첫 번째 토큰은 사용되지 않으므로, 이를 무시합니다.
    next(tokens)

    # 스택과 출력을 위한 리스트를 초기화합니다.
    stack =[]
    output = []

    # 스택과 출력 리스트에 대한 메서드를 미리 할당합니다
    push = stack.append
    append = output.append
    pop = stack.pop

    # 각 토큰에 대해 반복문을 실행합니다.
    for op in tokens:
        # 토큰이 '1'인 경우, 다음 토큰을 스택에 추가합니다.
        if op == b'1':
            push(next(tokens))

        # 토큰이 '2'인 경우, 스택에서 요소를 제거하고 출력 리스트에 추가합니다. 스택이 비어있는 경우 '-1'을 추가합니다.
        elif op == b'2':
            append(pop() if stack else b'-1')
        
        # 토큰이 '3'인 경우, 스택의 길이를 출력 리스트에 추가합니다.
        elif op == b'3':
            append(str(len(stack)).encode())

        # 토큰이 '4'인 경우, 스택이 비어있는지 확인하고 결과를 출력 리스트에 추가합니다.
        elif op == b'4':
            append(b'0' if stack else b'1')

        # 그 외 경우 , 스택의 마지막 요소를 출력 리스트에 추가합니다. 스택이 비어있는 경우 '-1'을 추가합니다.
        else:
            append(stack[-1] if stack else b'-1')

    # 출력 리스트의 요소를 개행 문자로 연결하여 표준 출력에 사용합니다
    os.write(1, b'\n'.join(output))

    # 프로그램을 종료합니다
    os._exit(0)

# main 함수를 호출합니다.
main()