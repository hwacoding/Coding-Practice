# 1. 아이디어
#  - 수열 : 백트래킹
#  - 중복 가능 : 뽑은거 체크할 필요x

# 2. 시간복잡도
#  - 중복 가능 = O(N^N) : 7^7 >> N이 8까지 가능하므로 가능!

# 3. 자료구조
#  - N, M : int
#  - tmp : print

import sys
input=sys.stdin.readline

N,M=map(int,input().split())
tmp=[0 for _ in range(M)]

def recur(lev):
    if lev==0:
        for i in tmp:
            print(i,end=" ")
        print()
        return
    
    for i in range(N):
        tmp[M-lev]=i+1
        recur(lev-1)

recur(M)