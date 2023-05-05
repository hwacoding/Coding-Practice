# 1. 아이디어
#  - 순간이동은 0초
#  - BFS
#  - Q에 현재 위치 순간 이동해서 갈 수 있는 위치 다 넣는다.
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
chk=[False]*100001

def bfs(st,en):
    Q=deque([])
    Q.append(st)
    chk[st]=True
    rs=0

    while Q:
        for i in range(len(Q)):
            j=1
            while 1:
                if Q[i]*2**j<100001 and chk[Q[i]*2**j]==False:
                    chk[Q[i]*2**j]=True
                    Q.append(Q[i]*2**j)
                    j+=1
                else:
                    break
        # print(Q)
        if en in Q:
            return rs

        L=len(Q)
        for i in range(L):
            K=Q.popleft()

            if K-1>=0 and chk[K-1]==False: # 위치가 0부터 시작하는 것 확인!
                chk[K-1]=True
                Q.append(K-1)
            if K+1<len(chk) and chk[K+1]==False:
                chk[K+1]=True
                Q.append(K+1)
        rs+=1

print(bfs(N,M))