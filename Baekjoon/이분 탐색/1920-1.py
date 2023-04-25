# 1. 아이디어
#  - 존재하는지 탐색 : 이분 탐색
#  - sort
#  - recur(st, en, target)
#  - mid > target : recur(mid+1,en,target)
#  - mid <= target : recur(st,mid, target)
#  - st==en : return

# 2. 시간복잡도
#  - Mlog(N)
#  - N = 100,000 : log(N) ~= 20
#  - M = 100,000

# 3. 자료구조
#  - N,M : int
#  - Narr,Marr : int[]

import sys
input=sys.stdin.readline

N=int(input())
Narr=list(map(int,input().split()))
Narr.sort()

M=int(input())
Marr=list(map(int,input().split()))

def recur(st,en,target):
    # print(Narr[st:en])
    if st==en:
        if Narr[st]==target:
            print(1)
        else:
            print(0)
        return

    mid=(st+en)//2

    if Narr[mid]<target:
        recur(mid+1,en,target)
    else:
        # --★ target과 같은 경우가 있기 때문에, recur(st,mid)로 재귀한다. ★--
        recur(st,mid,target) 

for i in range(M):
    recur(0,N-1,Marr[i])