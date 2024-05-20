# 백준
# 2750번 문제
# 수 정렬하기
# python 언어

# 전체코드
"""
사용자로부터 N개의 정수를 입력받아, 이를 오름차순으로 정렬하여 출력하는 역활을 합니다.
"""


# sys 모듈을 불러옵니다
import sys

# sys.stdin.readline을 input으로 재정의합니다. 이를 통해 입력을 더 빠르게 받을 수 있습니다.
input = sys.stdin.readline

# 사용자로부터 문자열을 입력받아 정수로 변환하고, 이를 N에 할당합니다
N = int(input())

# 정수들을 저장할 리스트 x를 초기화합니다
x = []

# N번 반복하는 반복문을 실행합니다
for i in range(0, N):
    #사용자로부터 문자열을 입력받아 정수로 변환하고,이를 리스트 x에 추가합니다.
    x.append(int(input()))

# 리스트 x를 오름차순으로 정렬합니다
x.sort()

# 리스트 x의 각 요소를 출력합니다.
for j in x:
    print(j)