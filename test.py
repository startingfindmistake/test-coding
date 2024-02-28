import sys
input = sys.stdin.readline

N,M,L = map(int, input(). split())
pnt = [int(input()) for _ in range(M)] + [L]
frd = [int(input()) for _ in range(N)]

def fun(mid):
    count,temp = 0,0
    for i in pnt:
        if i - temp >= mid:
            count += 1
            temp = i
    return count

for i in frd:
    start, end = 1, L
    ans = 0

    while start <= end:
        mid = (start + end)// 2
        count = fun(mid)


        if count > i:
            start = mid + 1
            ans = max(ans, mid)

        else:
            end = mid - 1
    print(ans)