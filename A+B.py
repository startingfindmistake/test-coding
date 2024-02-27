#A + B
#문제
#두 정수 A와 B를 입력받은 다음, A + B를 출력하는 프로그램을 작성하시오.

#입력
#첫째 줄에 A와 B가 주어진다.(0<A, B<10)

#출력
#첫째 줄에 A + B를 출력한다.

#예제 입력1
#1 2
#예제 출력1
#3

#전체코드
A, B = map(int, input().split())
print(A + B)


#A - B문제
#전체코드
A, B = map(int, input().split())
print(A - B)

#A * B문제
#전체코드
A, B = map(int, input().split())
print(A * B)

#A / B문제
#전체코드
A, B = map(float, input().split())
print(A / B)