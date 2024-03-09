문제
그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

출력
첫째 줄에 그룹 단어의 개수를 출력한다.

예제 입력 1 
3
happy
new
year
예제 출력 1 
3
예제 입력 2 
4
aba
abab
abcabc
a
예제 출력 2 
1
예제 입력 3 
5
ab
aa
aca
ba
bb
예제 출력 3 
4
예제 입력 4 
2
yzyzy
zyzyz
예제 출력 4 
0
예제 입력 5 
1
z
예제 출력 5 
1
예제 입력 6 
9
aaa
aaazbz
babb
aazz
azbz
aabbaa
abacc
aba
zzaz
예제 출력 6 
2


전체코드

def is_group_word(word):
    # 각 문자의 연속성을 확인하기 위한 set
    seen = set()
    prev_char = None

    for char in word:
        #이전 문자와 같다면 연속성 유지
        if char == prev_char:
            continue
        # 이전 문자와 다르다면
        else:
            # 이미 나온 문자인지 확인
            if char in seen:
                return False
            # 처음 나온 문자라면 추가
            seen.add(char)
            prev_char = char
    
    return True

# 입력 받기
N = int(input())
words = [input() for _ in range(N)]

# 그룹 단어 개수 세기
group_word_count = 0
for word in words:
    if is_group_word(word):
        group_word_count += 1


print(group_word_count)