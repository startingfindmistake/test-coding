# 백준
# 9935
# 문자열 폭발
# python 언어

"""
사용자로부터 문자열 word와 bomb을 입력받아, word에서 bomb와 일치하는 부분을 모두 제거하고
남은 문자열을 출력하느 역활을 합니다.
만약 word에서 bomb와 일치하는 부분이 없는 경우, 'FRULA'를 출력합니다.
"""

#sys 모듈을 불러옵니다.
import sys

# sys.stdin.readline을 input으로 재정의합니다. 이를 통해 입력을 더 빠르게 받을 수 있습니다.
input = sys.stdin.readline

# main 함수를 정의합니다.
def main():
    # 사용자로부터 문자열을 입력받아 양쪽 공백을 제거하고, 이를 word에 할당합니다.
    word = input().strip()

    # 사용자로부터 문자열을 입력받아 양쪽 공백을 제거하고, 이를 bomb에 할당합니다.
    bomb = input().strip()

    # 문자열을 bomb을 리스트 bomb_list로 변환합니다.
    bomb_list = list(bomb)

    # bomb의 길이를 length에 할당합니다.
    length = len(bomb)

    # bomb의 마지막 문자를 last에 할당합니다.
    last = bomb[-1]

    # 스택을 저장할 리스트 stack을 초기화합니다.
    stack = []

    # 문자열 word의 각 문자에 대해 반복문을 실행합니다.
    for i in word:
        # 현재 문자를 스택에 추가합니다.
        stack.append(i)

        # 현재 문자가 last와 같고, 스택의 마지막 length개의 요소가 bomb_list와 같은 경우
        if i == last and stack[-length:] == bomb_list:
            # 스택의 마지막 length개의 요소를 제거합니다.
            del stack[-length:]


    # 스택이 비어있지 않은 경우, 스택의 요소를 연결하여 문자열로 변환하고 출력합니다.
    # 스택이 비어잇는 경우, 'FRULA'를 출력합니다.
    print(''.join(stack) if stack else 'FRULA')


# main 함수를 호출합니다.
main()