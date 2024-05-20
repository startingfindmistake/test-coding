# 백준
# 1920
# 수 찾기
# python 언어

"""
사용자로부터 두 개의 문자열을 입력받아, 두 번째 문자열의 각 요소가 첫 번째 문자열의 요소 중
하나와 일치하는지를 확인하여, 일치하는 경우 '1'을, 그렇지 않은 경우 '0'을 출력하는 역활을 합니다.
"""
# sys 모듈을 불러옵니다
import sys

# sys.stdin.readline을 input으로 재정의합니다. 이를 통해 입력을 더 빠르게 받을 수 있습니다.
input = sys.stdin.readline

# sys.stdout.write를 output으로 재정의합니다. 이를 통해 출력을 더 빠르게 받을 수 있습니다.
output = sys.stdout.write

# 딕셔너리 a_dict를 초기화합니다
a_dict = dict()


# 첫 번째 줄의 입력은 사용되지 않으므로, 이를 무시합니다.
_ = input()


# 두 번째 줄의 입력을 공백으로 분리하고, 각 요소를 딕셔너리 a_dict의 키로 저장합니다. 각 키의 값은 0 입니다.
for a in input().split():
    a_dict[a] = 0

# 세 번째 줄의 입력은 사용되지 않으므로, 이를 무시합니다.
_ = input()

# 네 번째 줄의 입력을 공백으로 분리하고, 각 요소에 대해 반복문을 실행합니다.
for b in input().split():
    # 현재 요소가 딕셔너리 a_dict의 키인 경우
    if b in a_dict:
        # '1\n'을 출력합니다.
        output('1\n')
    # 그렇지 않은 경우
    else:
        # '0\n'을 출력합니다.
        output('0\n')
