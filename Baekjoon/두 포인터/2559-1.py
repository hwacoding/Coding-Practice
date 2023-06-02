# 1. 아이디어 
#  - 연속적 : 두 포인터
#  - 처음 구하고, left 빼고, right 더함
#  - 값 갱신

# 2. 시간복잡도
#  - O(N)

import sys
input=sys.stdin.readline

N,K=map(int,input().split())
A=list(map(int,input().split()))

res=0
for i in range(K):
    res+=A[i]
left=0
right=K-1

tmp=res
while 1:
    tmp-=A[left]
    left+=1 

    if right==len(A)-1:
        break
    right+=1
    tmp+=A[right]

    if tmp>res:
        res=tmp


print(res)