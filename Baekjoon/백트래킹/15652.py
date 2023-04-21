# 1. 아이디어
#  - 수열 => 백트래킹
#  - recur(lev)

# 2. 시간복잡도
#  - 중복가능 >> O(N^N) : N = 8

# 3. 자료구조
#  - N,M : int

import sys
input=sys.stdin.readline

N,M=map(int,input().split())
tmp=[10 for _ in range(M)]
res=[]

def recur(lev):
    if lev==0:
        for i in range(M):
            print(tmp[i],end=" ")
        print('')
        return
    
    for i in range(1,N+1):
        if M==lev:
            tmp[0]=i
            recur(lev-1)
        elif i>=tmp[M-lev-1]:
            tmp[M-lev]=i
            recur(lev-1)
        

recur(M)