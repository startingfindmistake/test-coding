# 백준
# 2738번 문제
# 행렬 덧셈
# python 언어

#전체코드

# sys 모듈을 불러옵니다
import sys

# sys.stdin.readline을 input으로 재정의합니다. 이를 통해 입력을 더 빠르게 받을 수 있습니다.
input = sys.stdin.readline

#사용자로부터 두 개의 정수를 입력받아 n과 m에 할당합니다.
n, m = map(int, input().split())

# n개의 줄에 걸쳐 정수들을 입력받아 2차원 리스트 a를 생성합니다.
a = [list(map(int, input().split())) for _ in range(n)]

# n개의 줄에 걸쳐 정수들을 입력받아 2차원 리스트 b를 생성합니다.
b = [list(map(int, input().split())) for _ in range(n)]

# 각 요소에 대해 a[i][j]와 b[i][j]를 더하여 a[i][j]를 업데이트 합니다
for i in range(n):
    for j in range(m):
        a[i][j] += b[i][j]

# 업데이트된 2차원 리스트 a를 출력합니다
for i in a:
    print(*i)
    