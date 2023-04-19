# 1. 아이디어
#  - BFS
#  - 간선 연결 그래프
#  - 하나씩 확인. chk==0 and mp[i][]==1 => for문

# 2. 시간복잡도
#  - O(V+E) -> 간선 그래프 확인해야하므로 V=N*(N-1)/2
#  - 999000/2*2 >> 가능

# 3. 자료구조
#  - N,M : int
#  - mp : int[][]
#  - chk : int[]

import sys
sys.setrecursionlimit(10**9)
# --★ 재귀함수일 경우 설정해두기 ★--
input=sys.stdin.readline

N,M=map(int,input().split())
mp=[[0 for _ in range(N+1)] for _ in range(N+1)]
chk=[0 for _ in range(N+1)]

for i in range(M):
    a,b=map(int,input().split())
    mp[a][b]=1
    mp[b][a]=1

def bfs(y):
    for i in range(1,N+1): # x
        if mp[y][i]==1 and chk[i]==0:
            chk[i]=1
            bfs(i)

cnt=0
for i in range(1,N+1): # y
    if chk[i]==0:
        chk[i]=1
        bfs(i)
        cnt+=1

print(cnt)