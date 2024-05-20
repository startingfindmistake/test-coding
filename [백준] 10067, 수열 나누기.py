# 백준
# 10067
# 수열 나누기
# pypy언어


#복잡한 동적 프로그래밍 문제를 해결하는 데 사용되며, 특히 선분들의 교점을 찾는 데 사용합니다.
#이러한 과정을 "Convex Hull Trick'이라고도 불립니다.
#이러한 과정을 통해 특정 조건 하에서 최적의 해를 찾는 문제에 사용됩니다.


def divisionOfSequence():
    # 표준 입력과 출력을 엽니다.
    stdin = open(0)
    stdout = open(1,'w')

    # n과 k를 입력받습니다.
    n,k = map(int,next(stdin).split())

    # 배열 arr를 입력받습니다.
    arr = map(int,next(stdin).split())

    # 누적 합 배열 s를 초기화합니다.
    s = [0]*(n+1)
    for i in range(1,n+1):
        s[i] = s[i-1]+next(arr)

    # 동적 프로그래밍 테이블 dp와 추적 테이블 trace를 초기화합니다.
    dp = [[0]*(n+1)for _ in range(2)]
    trace = [[0]*(n+1)for _ in range(k+1)]

    # pp, qq, ss, nn 배열을 초기화합니다.
    pp,qq,ss,nn = ([0]*n for _ in range(4))

    # inter 함수를 정의합니다. 이 함수는 두 선분의 교점을 찾습니다.
    def inter(idx):
        return (cq-qq[idx])/(pp[idx]-cp)

    # k까지 반복하면서 동적 프로그래밍 테이블을 채웁니다.
    for c in range(1,k+1):
        top = work = 0

        for i in range(1,n+1):
            cp,cq,cs,cn = s[i-1],dp[c-1&1][i-1]-s[i-1]*s[i-1],0,i-1

            # 현재 선분과 이전 선분이 같은 기울기를 가지고 있지만 y절편이 다른 경우, 이전 선분을 제거합니다.
            if top and (pp[top-1]==cp) and (qq[top-1]<cq):
                top -= 1
                if top==work: work -= 1

            # 현재 선분과 이전 선분이 다른 기울기를 가지는 경우, 이전 선분을 제거하고 새로운 선분을 추가합니다.
            while top and (pp[top-1]!=cp):
                cs = inter(top-1)
                if ss[top-1] < cs: break
                top -= 1
                if top==work: work -= 1

            if top==0 or (top and pp[top-1]!=cp):
                pp[top],qq[top],ss[top],nn[top] = cp,cq,cs,cn
                top += 1

            x = s[i]

            # 현재 x값에 대해 최적의 선분을 찾습니다.
            while work+1 < top and ss[work+1] < x: work += 1
            dp[c&1][i] = pp[work] * x + qq[work]
            trace[c][i] = nn[work]

    # 최종 결과를 출력합니다.
    stdout.write(f'{dp[k&1][n]}\n')

    # 추적 테이블을 이용하여 선택된 원소들을 찾습니다.
    rec = []
    cur = n
    for i in range(k,0,-1):
        rec.append(trace[i][cur])
        cur = trace[i][cur]
    rec.sort()

    # 선택된 원소들을 조정합니다.
    for i in range(k):
        if rec[i]==0: rec[i] = 1
        if i and rec[i]<=rec[i-1]: rec[i] = rec[i-1]+1

    # 선택된 원소들을 출력합니다.
    stdout.write(' '.join(map(str,rec)))

divisionOfSequence()

