# 백준
# 10256
# 돌연변이
# pypy3 언어


# 함수를 정의하여 마커와 돌연변이를 생성하는 부분

def generate_mutations(marker):
    mutations = set()  # 중복된 돌연변이를 방지하기 위해 세트(set)를 사용합니다.
    n = len(marker)
    
    # 두 번째 부분을 뒤집는 모든 경우의 수를 생성
    for i in range(n + 1):
        for j in range(n + 1):
            # 마커의 일부를 뒤집어 돌연변이를 생성합니다.
            mutated_marker = marker[:i] + marker[i:j][::-1] + marker[j:]
            mutations.add(mutated_marker)  # 생성된 돌연변이를 세트에 추가합니다.
    
    return mutations

# 주어진 DNA 구조에서 마커와 돌연변이가 몇 번 출현하는지 세는 함수

def count_mutations(dna, marker):
    mutations = generate_mutations(marker)  # 모든 돌연변이를 생성합니다.
    count = 0  # 출현 횟수를 저장할 변수를 초기화합니다.
    
    for i in range(len(dna) - len(marker) + 1):
        substring = dna[i:i + len(marker)]  # DNA 문자열에서 마커와 같은 길이의 부분 문자열을 추출합니다.
        if substring in mutations:  # 추출한 부분 문자열이 돌연변이 중에 있다면,
            count += 1  # 출현 횟수를 증가시킵니다.
    
    return count

# 테스트 케이스 수 입력
T = int(input())

for _ in range(T):
    # DNA 구조와 마커 입력
    n, m = map(int, input().split())  # DNA 길이와 마커 길이를 입력받습니다.
    dna = input()  # DNA 문자열을 입력받습니다.
    marker = input()  # 마커를 입력받습니다.
    
    # 결과 출력
    result = count_mutations(dna, marker)  # DNA에서 마커와 돌연변이가 몇 번 출현하는지 계산합니다.
    print(result)  # 결과를 출력합니다.
