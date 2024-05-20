# 백준
# 11066
# 파일 합치기
# python 언어

"""
사용자로부터 T개의 테스트 케이스를 입력받아, 각 테스트 케이스에 대해 k개의 파일을 합치는데 필요한
최소 비용을 계산하여 출력하는 역활을 합니다.
"""

# sys 모듈을 불러옵니다.
import sys

# solution 함수를 정의합니다.
def solution():
    # 표준 입력을 바이너리 읽기 모드로 엽니다.
    stdin = open(0, "rb")

    # 첫 번재 줄의 입력을 읽어 정수로 변환하고, 이를 T에 할당합니다.
    T = int(stdin.readline())

    # T번 반복하는 반복문을 실행합니다.
    for _ in range(T):
        # 두 번째 줄의 입력을 읽어 정수로 변환하고, 이를 k에 할당합니다.
        k = int(stdin.readline())

        #세 번째 줄의 입력을 공백으로 분리하고, 각 요소를 정수로 변환하여 리스트 sizes를 생성합니다.
        sizes = list(map(int, stdin.readline().split()))


        # ans와 cursor를 초기화합니다.
        ans = 0
        cursor = 1

        # 큐 q를 초기화합니다
        q = [1_000_000_000, sizes[0]] + [0] * k

        # combine 함수를 정의합니다. 이 함수는 큐의 end 위치의 요소와 그 앞의 요솔르 합칩니다.
        def combine(end):
            nonlocal ans
            nonlocal cursor

            # cost를 계산합니다.
            cost = q[end-1] + q[end]

            # ans에 cost를 더합니다.
            ans += cost

            # 큐에서 end 위치의 요소를 제거합니다.
            q.pop(end)

            # i를 초기화합니다
            i = end -2

            # 큐의 i 위치의 요소가 cost보다 작은 동안 반복문을 실행합니다.
            while q[i] < cost:
                i -= 1

            # 큐를 업데이트합니다
            q[i+2: end] = q[i+1: end-1]
            q[i+1] = cost

            # cursor를 갱신합니다.
            cursor -= 1

            # i가 0보다 크고, 큐의 i-1 위치의 요소가 cost 이하인 동안 반복문을 실행합니다.
            while i > 0 and q[i-1] <= cost:
                d = cursor-i
                combine(i)
                i = cursor-d
        
        # 리스트의 sizes의 각 요소에 대해 반복문을 실행합니다.
        for x in sizes[1:]:
            # 큐의 cursor-1 위치의 요소가 x 이하인 동안 반복문을 실행합니다.
            while q[cursor-1] <= x:
                combine(cursor)

            
            # cursor를 증가시키고, 큐의 cursor 위치에 x를 저장합니다.
            cursor += 1
            q[cursor] = x

        # cursor가 1보다 큰 동안 반복문을 실행합니다.
        while cursor > 1:
            combine(cursor)

        # 최종 결과값을 출력합니다.
        print(ans)

## enddef solution

# solution 함수를 호출합니다.
solution()

