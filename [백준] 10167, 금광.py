# 백준
# 10167
# 금광
# python 언어


"""
2차원 평면에서 가장 큰 합을 가지는 부분 집합을 찾는 문제를 해결합니다.
이 문제는 동적 프로그래밍과 세그먼트 트리를 사용하여 해결할 수 있습니다.
"""

import sys,math

# n을 입력받습니다.
n=int(sys.stdin.readline())
ix=[];iy=[];iw=[]
# n개의 점에 대한 정보를 입력받습니다.
for i in range(n):
	x,y,w=map(int,sys.stdin.readline().split())
	ix.append(x)
	iy.append(y)
	iw.append(w)

# x와 y의 중복을 제거한 후, 각각의 길이를 구합니다.
nx=len(set(ix));ny=len(set(iy))
# x와 y의 값을 인덱스로 변환합니다.
tx=dict(zip(sorted(list(set(ix))),[i for i in range(nx)]))
ty=dict(zip(sorted(list(set(iy))),[i for i in range(ny)]))

# 각 x에 대한 (y, w)를 저장합니다.
gold={}
for x,y,w in zip(ix,iy,iw):
	if tx[x] in gold.keys():
		gold[tx[x]].append((ty[y],w))
	else:
		gold[tx[x]]=[(ty[y],w)]

# 세그먼트 트리의 크기를 결정합니다.
s=1
while s<=ny:
	s=s<<1

# 세그먼트 트리를 업데이트하는 함수를 정의합니다.
def update(t,v):
	for i in range(4):
		stree[t][i]+=v
	t=t>>1
	while t>0:
		lv=stree[t<<1]
		rv=stree[t<<1|1]
		stree[t][0]=lv[0]+rv[0]
		stree[t][2]=max(lv[2],lv[0]+rv[2])
		stree[t][3]=max(rv[3],rv[0]+lv[3])
		stree[t][1]=max(lv[1],rv[1],lv[3]+rv[2])

		t=t>>1

# 가장 큰 합을 찾습니다.
m=0
for x1 in range(nx):
	stree=[[0,0,0,0] for i in range(ny<<2)]
	for x2 in range(x1,nx):
		for y,w in gold[x2]:
			update(s+y,w)
		m=max(m,stree[1][1])
# 결과를 출력합니다.
print(m)
