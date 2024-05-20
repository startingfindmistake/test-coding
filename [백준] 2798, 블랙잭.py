# 백준
# 2798번 문제
# 블랙잭
# python 언어

# 전체코드
"""
이 코드는 사용자로부터 입력받은 'n'개의 카드 중에서 세 개를 골라 그 합이 'm'을 넘지 않는
가장 큰 수를 찾는 역활을 합니다.
"""

# sys 모듈에서 stdin을 불러옵니다.
from sys import stdin

# 사용자로부터 두 개의 정수를 입력받아 n과 m에 할당합니다.
n, m = map(int, stdin.readline().split())

# 사용자로부터 n개의 정수를 입력받아 리스트 cards를 생성합니다.
cards = list(map(int, stdin.readline().split()))

# cards를 내림차순으로 정렬합니다.
cards.sort(reverse=True)

# 결과값을 저장할 변수 ans를 초기화합니다.
ans = 0

# cards의 각 세 개의 요소에 대해 반복문을 실행합니다.
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            # 세 개의 요소의 합을 total에 저장합니다.
            total = cards[i] + cards[j] + cards[k]

            # total이 m 이하인 경우
            if total <= m:
                # ans와 total 중 더 큰 값을 ans에 저장합니다.
                ans = max(ans, total)

                # 현재 반복문을 종료합니다
                break


# 최종 결과값을 출력합니다.
print(ans)