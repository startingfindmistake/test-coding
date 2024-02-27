#문제 제한 사항
#line의 세로(행)길이는 2 이상 1,000 이하인 자연수 입니다.
# -line의 가로(열)길이는 3 입니다
# - line의 각 원소는 [A, B C]형태 입니다
# - A, B, C는 -100,000 이상 100,000 이하인 정수입니다.
# - 무수히 많은 교점이 생기는 직선 쌍은 주어지지 않습니다.
# - A = 0이면서 B = 0인 경우는 주어지지 않습니다.

#정답은 1,000 * 1,000 크기 이내에서 표현됩니다.
#별이 한 개 이상 그려지는 입력만 주어집니다.

#1. 주어진 직선에서 교점을 구합니다.
for i in range(n):
    a, b, e = line[i]
    for j in range(i + 1, n):
        c, d, f = line[j]
        if a * d == b * c: continue
        x = (b * f - e * d) / (a * d - b * c)
        y = (e * c - a * f) / (a * d - b * c)


#2. 그중 정수 교점만 따로 변수로 저장합니다.
        if x == int(x) and y == int(y):
            x = int(x)
            y = int(y)
            pos.append([x, y])


#3. 교점을 모두 표현할 수 있는 최소한의 사각형을 알아냅니다.
            if x_min > x : x_min = x
            if y_min > y : y_min = y
            if x_max < x : x_max = x
            if y_max < y : y_max = y


#4. 모든 교점을 *로 찍어서 표현합니다.
            #파이썬에서는 고정된 리스트를 생성하는 방법이 없습니다.
            #for 문을 사용해 직접 할당하거나 리스트의 곱셈 또는 컴프리헨션 방식으로 생성해야 합니다.

            x_len = x_max - x_min + 1
            y_len = y-max - y_min + 1
            coord = [['.'] * x_len for _ in range(y_len)]

            for star_x, star_y in pos:
                nx = star_x + abs(x_min) if x_min < 0 else star_x - x_min
                ny = star_y + abs(y_min) if y_min < 0 else star_y - y_min
                coord[ny][nx] = '*'

            #5. 배열을 거꾸로 뒤집어 반환합니다.
                #마지막으로 나온 answer배열을 return하려고 하니 정답을 역순으로 제출해야 한다
                #이럴 경우 [].reverse() 또는 reversed([])를 사용하거나, 슬라이싱을 사용해[::-1]을 붙여 반대로 출력하도록 합니다.
                for result in coord:
                    answer.append(''.join(result))

                return answer[::-1]


#전체 코드
def solution(line):
    #prevent swallow copy
    pos, answer = [], []
    n = len(line)
    
    x_min = y_min = int(1e15)
    x_max = y_max = -int(1e15)
    
    for i in range(n):
        a, b, e = line[i]
        for j in range(i + 1, n):
            c, d, f = line[j]
            if a * d == b * c:
                continue
                
            x = (b*f - e*d) / (a*d - b*c)
            y = (e*c - a*f) / (a*d - b*c)

            if x == int(x) and y == int(y):
                x = int(x)
                y = int(y)
                pos.append([x,y])
                if x_min > x: x_min = x
                if y_min > y: y_min = y
                if x_max < x: x_max = x 
                if y_max < y: y_max = y 

    x_len = x_max - x_min + 1
    y_len = y_max - y_min + 1
    coord = [['.'] * x_len for _ in range(y_len)]

    for star_x, star_y in pos:
        nx = star_x + abs(x_min) if x_min < 0 else star_x - x_min
        ny = star_y + abs(y_min) if y_min < 0 else star_y - y_min
        coord[ny][nx] = '*'
        
    for result in coord: answer.append(''.join(result))

    return answer[::-1]




# 테스트 1
# 입력값 〉	[[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
# 기댓값 〉	["....*....", ".........", ".........", "*.......*", ".........", ".........", ".........", ".........", "*.......*"]
# 실행 결과 〉	테스트를 통과하였습니다.
# 테스트 2
# 입력값 〉	[[0, 1, -1], [1, 0, -1], [1, 0, 1]]
# 기댓값 〉	["*.*"]
# 실행 결과 〉	테스트를 통과하였습니다.
# 테스트 3
# 입력값 〉	[[1, -1, 0], [2, -1, 0]]
# 기댓값 〉	["*"]
# 실행 결과 〉	테스트를 통과하였습니다.
# 테스트 4
# 입력값 〉	[[1, -1, 0], [2, -1, 0], [4, -1, 0]]
# 기댓값 〉	["*"]

#수정본