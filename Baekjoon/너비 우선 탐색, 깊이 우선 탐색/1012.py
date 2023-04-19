# 1. 아이디어
#  - BFS
#  - chk==0 and mp==1 : BFS
#  - main : cnt+=1

# 2. 시간복잡도
#  - O(V+E)=O(N*M*5) : 12500 >> 가능!

# 3. 자료구조
#  - mp : int[][]
#  - chk : int[][]
#  - cnt : int

import sys
sys.setrecursionlimit(10**6) # default : 재귀 깊이 최대 1000
                             # setrecursionlimit으로 제한 변경
input=sys.stdin.readline

T=int(input())
cnt=0

dy=[1,0,-1,0]
dx=[0,1,0,-1]

def bfs(y,x):
    for k in range(4):
        ny=y+dy[k]
        nx=x+dx[k]
        if 0<=ny<N and 0<=nx<M:
            if mp[ny][nx]==1 and chk[ny][nx]==0:
                chk[ny][nx]=1
                bfs(ny,nx)

for t in range(T):
    N,M,K=map(int,input().split())
    mp=[[0 for _ in range(M)] for _ in range(N)]
    chk=[[0 for _ in range(M)] for _ in range(N)]
    for k in range(K):
        y,x=map(int,input().split())
        mp[y][x]=1
    
    for i in range(N):
        for j in range(M):
            if mp[i][j]==1 and chk[i][j]==0:
                chk[i][j]=1
                bfs(i,j)
                cnt+=1

    print(cnt)
    cnt=0