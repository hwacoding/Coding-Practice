# 1. 아이디어
#  - 백트래킹 recur(num), num은 현재 들어간 값
#  - 방문한 곳이 아니고, 앞서 저장된 값보다 크면, 저장 => 현재 들어간 값 이후부터 for문
#  - 전에 저장한 것 제거 및 방문도 False
#  - lev==M 이면, print

# 2. 시간복잡도
#  - O(N!) >> 가능!
     
# 3. 자료구조
#  - chk : bool[]
#  - res : int[]

import sys
input=sys.stdin.readline

N,M=map(int,input().split())
chk=[False]*(N+1)
res=[]

def recur(num): # num = 현재 들어간 값
    if len(res)==M: # 저장한 값이 M개이면, print
        print(' '.join(map(str,res)))
        return
    
    for i in range(num,N+1): # 현재 들어간 값 이후부터 for문
        if chk[i]==False:
            chk[i]=True
            res.append(i)
            recur(i)
            chk[i]=False
            res.pop()

recur(1)
