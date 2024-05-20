# 백준
# 5086번 문제
# 배수와 약수
# python 언어

# 전체코드

"""
이 코드는 사용자로부터 두 개의 정수를 입력받아, 한 숫자가 다른 숫자의 배수인지, 약수인지,
또는 둘 다 아닌지를 판단하여 출력하는 역활을 합니다.
"""

# 무한 반복문을 시작합니다.
while(1):

    # 사용자로부터 두 개의 정수를 입력받아 N과 M에 할당합니다.
    N, M = map(int, input().split())

    # 만약 N과 M이 모두 0이면 반복문을 종료합니다.
    if N == 0 and M == 0:
        break

    # 만약 M이 N의 배수이면 'factor' 를 출력합니다.
    if M % N == 0:
        print('factor')
    
    # 만약 N이 M의 배수이면 'multiple'를 출력합니다
    elif N % M == 0:
        print('multiple')
    
    # 위의 두 경우가 아니면 'neither'를 출력합니다.
    else:
        print('neither')
