# 1. 아이디어
#  - 상근이 카드 정렬
#  - 숫자 카드 하나씩 확인 : 이분 탐색

# 2. 시간복잡도
#  - O(Nlog(N))
#  - O(Mlog(N))
#  - (N+M)log(N) = 1e6*20 = 2천만 >> 가능!

import sys
input=sys.stdin.readline

N=int(input())
Nnums=list(map(int,input().split()))

M=int(input())
Mnums=list(map(int,input().split()))

Nnums.sort()

def half(st,ed,target):
    if st==ed:
        if Nnums[st]==target:
            print(1,end=" ")
        else:
            print(0,end=" ")
        return

    mid = (st+ed)//2

    if Nnums[mid]<target:
        half(mid+1,ed,target)
    else:
        half(st,mid,target)

for i in range(M):
    half(0,len(Nnums)-1,Mnums[i])