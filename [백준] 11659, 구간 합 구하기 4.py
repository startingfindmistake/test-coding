# 백준
# 11659
# 구간 합 구하기 4
# python 언어


# 전체 코드
"""
사용자로부터 n개의 정수와 m개의 쿼리를 입력받아, 각 쿼리에 대해 주어진 구간의 합을 출력하는 역활을 합니다.
"""

# PartSum 함수를 정의합니다. 이 함수는 구간의 합을 계산합니다.
def PartSum():
    # sys 모듈을 불러옵니다.
    import sys

    # 사용자로부터 두 개의 정수를 입력받아 n과 m에 할당합니다.
    n, m = map(int, input().split())

    # 사용자로부터 n개의 정수를 입력받아 리스트 lst를 생성합니다.
    lst = list(map(int, input().split()))

    # 리스트 lst의 첫 번째 위치에 0을 추가합니다.
    lst.insert(0,0)

    # 동적 프로그래밍을 위한 리스트 dp를 초기화합니다.
    dp = [0] * 100001

    # 1부터 n+1 까지의 숫자에 대해 반복문을 실행합니다
    for i in range(1, n + 1):
        # dp[i]에 lst[i]와 dp[i -1]의 합을 저장합니다.
        dp[i] = lst[i] + dp[ i - 1]

    # m번 반복하는 반복문을 실행합니다
    for _ in range(m):
        # 사용자롭퉈 두 개의 정수를 입력받아 id1과 id2에 할당합니다.
        id1, id2 = map(int, sys.stdin.readline().split())

        #dp[id2]와 dp[id1 - 1]의 차를 출력합니다.
        print(dp[id2] - dp[id1 - 1])

#PartSum 함수를 호출합니다
PartSum()