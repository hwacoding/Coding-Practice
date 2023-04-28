# 1. 아이디어
#  - 순간이동, -1, +1
#  - BFS
#  - 방문하지 않은 곳만 Queue에 추가

# 2. 시간복잡도
#  - 방문하지 않은 곳만 추가되기 때문에
#  - O(N)

# 3. 자료구조
#  - N, K : int
#  - chk : int[]

import sys
from collections import deque
input=sys.stdin.readline

N,K=map(int,input().split())
chk=[False]*100001

Q=deque([])
res=0

def bfs(st,en):
    global K
    global res

    Q.append(st)
    chk[st]=True
    sw=False

    while Q:
        # print(Q)
        for i in range(len(Q)):
            p=Q.popleft()

            if p==en:
                sw=True
                break
            if 2*p<len(chk) and chk[2*p]==False:
                chk[2*p]=True
                Q.append(2*p)
            if p+1<len(chk) and chk[p+1]==False:
                chk[p+1]=True
                Q.append(p+1)
            if p>0 and chk[p-1]==False:
                chk[p-1]=True
                Q.append(p-1)
        
        if sw==True:
            break
        res+=1


bfs(N,K)

print(res)