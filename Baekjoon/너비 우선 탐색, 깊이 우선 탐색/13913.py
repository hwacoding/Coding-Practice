# 1. 아이디어
#  - 순간이동도 1초
#  - BFS
#  - Q에 N+1, N-1, 2*N 넣는다.
#  - N 최대치 넘지 않고, 방문하지 않은 곳을 계속 Q에 넣고 반복.

# 2. 시간복잡도
#  - BFS : O(V+E)
#  - O(N)

# 3. 변수
#  - N,K : int
#  - chk[] : int

import sys
from collections import deque
input=sys.stdin.readline

N,M=map(int,input().split())
chk=[0]*100001

def bfs(st,en):
    Q=deque([])
    Q.append(st)
    chk[st]=-1
    rs=0

    while Q:
        # print(Q)
        if en in Q:
            return rs
        else:
            L=len(Q)
            for i in range(L):
                K=Q.popleft()

                if K+1<len(chk) and chk[K+1]==0:
                    chk[K+1]=K
                    Q.append(K+1)
                if K-1>=0 and chk[K-1]==0:
                    chk[K-1]=K
                    Q.append(K-1)
                if 2*K<len(chk) and chk[2*K]==0:
                    chk[2*K]=K
                    Q.append(2*K)
        
        rs+=1

rs=bfs(N,M)
print(rs)

root=[M]
for i in range(rs):
    k=root[len(root)-1]
    root.append(chk[k])

for i in range(len(root)-1,-1,-1):
    print(root[i],end=' ')