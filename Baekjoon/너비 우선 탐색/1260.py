
# 1. 아이디어
#  DFS
#  - 시작 정점에서 출발
#  - 간선 연결도에서 Y축을 기준 현재 정점
#  - X축에서 연결된 정점으로 계속 이동 후, 1이 없거나 방문한 곳이면 끝.
#  - for문 순으로 가기 때문에 정점 번호가 작은 것부터 방문하게 된다.

#  BFS
#  - 간선 연결도에서 Y축 기준 1인 정점 모두 Queue에 저장
#  - Queue 꺼낸 정점으로 이동(Y축)
#  - 방문한 곳이 아니면, Queue에 저장.

# 2. 시간복잡도
#  - DFS, BFS : O(V+E)
#  - V : N*M 
#  - E : 4*V = 4*N*M
#  - V+E = 5*N*M = 5,000,000 < 2억 >> 가능!

# 3. 자료구조
#  - 그래프 저장 : int[][]
#  - 방문 여부 : bool[][]
#  - Queue : BFS
#  - DFS 방문 저장 : int[]

import sys
input=sys.stdin.readline

N,M,V=map(int,input().split())
V-=1
mp=[[0 for _ in range(N)] for _ in range(N)]
chk=[False]*N # 방문한 정점

for i in range(M):
    y,x=map(int,input().split())
    mp[y-1][x-1]=1
    mp[x-1][y-1]=1 #양방향 간선


def dfs(V):
    for i in range(N):
        if mp[V][i]==1 and chk[i]==False:
            # 방문 체크
            chk[i]=True
            visited.append(i+1)
            dfs(i)


def bfs(V):
    q=[V]

    while q:
        V=q[0] # 먼저 들어온 정점부터
        del q[0] 

        for i in range(N):
            if mp[V][i]==1 and chk[i]==False:
                chk[i]=True
                q.append(i)

        visited.append(V+1)

# DFS
chk[V]=True
visited=[V+1]
dfs(V)

# DFS 출력
for i in visited:
    print(i,end=" ")
print()

# BFS
chk=[False]*N
chk[V]=True
visited=[]
bfs(V)

# BFS 출력
for i in visited:
    print(i,end=" ")