# 1. 아이디어
#  - BFS(V)
#  - 연결된 방문하지 않은 노드로 탐색

# 2. 시간복잡도
#  - O(V+E) = 100+100*50 < 2억 >> 가능!

#  3. 자료구조
#  - mp : 간선 연결도
#  - chk : 방문 체크
#  - cnt : int

import sys
input=sys.stdin.readline

N=int(input())
M=int(input())
mp=[[0 for _ in range(N)] for _ in range(N)]
chk=[False]*N
chk[0]=True # 1번 컴퓨터에서 시작

for i in range(M):
    a,b=map(int,input().split())
    mp[a-1][b-1]=1
    mp[b-1][a-1]=1

cnt=0

def bfs(v):
    global cnt

    for i in range(N):
        if mp[v][i]==1 and chk[i]==False:
            chk[i]=True
            cnt+=1
            bfs(i)

bfs(0)
print(cnt)