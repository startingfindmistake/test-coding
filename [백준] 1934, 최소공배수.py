# 백준
# 1934번 문제
# 최소공배수
# python 언어


# 전체코드
"""
사용자로부터 T개의 정수 쌍을 입력받아, 각 정수 쌍의 최소공배수를 출력하는 역활을 합니다
"""


# sys 모듈을 불러옵니다
import sys

# 사용자로부터 문자열을 입력받아 정수로 변환하고, 이를 T에 할당합니다
T = int(sys.stdin.readline())

# T 번 반복하는 반복문을 실행합니다
for _ in range(T):
    # 사용자로부터 두 개의 정수를 입력받아 a와 b에 할당합니다
    a, b = map(int, sys.stdin.readline().split())

    # a와 b를 x와 y에 할당합니다.
    x, y = a, b
    # x가 y보다 작은 경우, x 와 y를 교한합니다.
    if x < y:
        x, y = y, x

    # y가 0보다 큰 동안 반복문을 실행합니다.
    while y > 0:
        # x를 y로 나눈 나머지를 i에 저장합니다
        i = x % y

        # y를 x에 할당합니다
        x = y

        # i를 y에 할당합니다
        y = i

    # a 와 b의 곱을 x로 나눈 몫을 출력합니다.
    print(a * b // x)
    