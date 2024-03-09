문제
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

입력
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

출력
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

예제 입력 1 
Mississipi
예제 출력 1 
?
예제 입력 2 
zZa
예제 출력 2 
Z
예제 입력 3 
z
예제 출력 3 
Z
예제 입력 4 
baaa
예제 출력 4 
A


# 이 문제는 주어진 단어에서 가장 많이 사용된 알파벳으 찾는 것입니다.
# 대소문자를 구분하지 않으며, 가장 많이 사용된 알파벳이 여러 개인 경우 '?'를 출력합니다.

전체코드

# 사용자로부터 입력 받기
word = input().upper()

# 알파벳별 빈도수 계산
counts = {chr(i): word.count(chr(i)) for i in range(65, 91)}

# 가장 많이 사용된 알파벳 찾기
max_count = max(counts.values())
max_chars = [k for k, v in counts.items() if v == max_count]

# 결과 출력
if len(max_chars) > 1:
    print('?')
else:
    print(max_chars[0])
