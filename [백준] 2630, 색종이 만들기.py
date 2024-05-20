# 백준
# 2630
# 색종이 만들기
# python 언어

"""
사용자로부터 n과 nxn 크기의 맵을 입력받아, 맵을 흰색과 파란색 종이로 분할하여 
흰색 종이와 파란색 조잉의 개수를 계산하여 출력하는 역활을 합니다.
"""

# solve 함수를 정의합니다. 이 함수는 분할 정복 알고리즘을 사용하여 흰색과 파란색 종이의 개수를 계산합니다.
def solve(map, x, y, n):
    # 종료 조건: n이 1인 경우
    if n == 1:
        # map[y][x]가 1인 경우, 파란색 종이가 1개 있음을 반환합니다.
        if map[y][x] == 1:
            return(0,1)
        # 그렇지 않은 경우, 흰색 종이가 1개 있음을 반환합니다.
        else:
            return(1, 0)
        

    # 분할: n을 2로 나누어 네 개의 부분 문제를 생성합니다.
    d = n // 2
    w1, b1 = solve(map, x, y, d)
    w2, b2 = solve(map, x + d, y, d)
    w3, b3 = solve(map, x, y + d, d)
    w4, b4 = solve(map, x + d, y + d, d)

    # 병합: 네 개의 부분 문제의 결과를 병합니다.
    wsum = w1 + w2 + w3 + w4
    bsum = b1 + b2 + b3 + b4

    # 모든 부분 문제에서 흰색 종이만 있는 경우
    if wsum == 4 and bsum == 0:
        return(1, 0)
    
    # 모든 부분 문제에서 파란색 종이만 있는 경우
    elif wsum == 0 and bsum == 4:
        return (0, 1)
    
    # 그렇지 않은 경우, 흰색 종이와 파란색 종이의 개수를 그대로 반환합니다.
    else:
        return(wsum, bsum)
    

    # debugMap 함수를 정의합니다. 이 함수는 맵을 출력합니다
    def debugMap(map, n):
        for y in range(n):
            for x in range(n):
                print(map[y][x], end=" ")
            print()

# 맵을 저장할 리스트 m을 초기화합니다.
m = list()

# 사용자로부터 문자열을 입력받아 정수로 변환하고, 이를 n에 할당합니다
n = int(input())


# n번 반복하는 반복문을 실행합니다.
for i in range(n):
    # 사용자로부터 n개의 정수를 입력받아 리스트 m에 추가합니다.
    m.append(list(map(int, input().split())))


# solve 함수를 호출하여 흰색 종이와 파란색 종이의 개수를 계산하고, 이를 출력합니다.
white, blue = solve(m, 0, 0, n)
print(white)
print(blue)
    