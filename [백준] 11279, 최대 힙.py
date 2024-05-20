# 백준
# 11279
# 최대 힙
# python 언어

"""
사용자로부터 N개의 정수를 입력받아, 각 정수가 0 인 경우 힙에서 가장 큰 요소를 제거하고 출력하고,
그렇지 않은 경우 해당 정수를 힙에 추가하는 역활을 합니다.
"""

# sys 모듈을 불러옵니다.
import sys

# heapq 모듈을 불러옵니다
import heapq

# 사용자로부터 문자열을 입력받아 정수로 변환하고, 이를 N에 할당합니다.
N = int(sys.stdin.readline())

# 힙을 저장할 리스트 heap을 초기화합니다.
heap = []

# N번 반복하는 반복문을 실행합니다.
for _ in range(N):

    # 사용자로부터 문자열을 입력받아 정수로 변환하고, 이를 x에 할당합니다.
    x = int(sys. stdin. readline())

    # x가 0인 경우
    if x == 0:

        # heap이 비어있지 않은 경우
        if heap:

            # heap에서 가장 작은 요솔르 제거하고, 이를 출력합니다.
            # heap에 저장된 요소는 음수이므로, 출력할 때 부호를 바꿉니다.
            print(-heapq.heappop(heap))

        # heap이 비어있는 경우
        else:

            #'0'을 출력합니다.
            print('0')

    # x가 0이 아닌 경우
    else:

        # x를 heap에 추가합니다.
        # x는 음수로 저장되므로, heap에서 가장 작은 요소가 실제로는 가장 큰 요소입니다.
        heapq.heappush(heap, -x)