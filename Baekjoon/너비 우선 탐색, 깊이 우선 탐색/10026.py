# 1. 아이디어
#  - DFS
#  - 전체 돌면서 구역 확인
#  - 적록색약인 사람은 R, G 같은 구역으로

# 2. 시간복잡도
#  - O(V+E) = 50000

import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

N=int(input())
mp=[input().strip() for _ in range(N)] # 문자열 strip으로 \n 제거해서 읽어온다.
chk=[[False]*N for _ in range(N)]

dy=[0,1,0,-1]
dx=[1,0,-1,0]
def DFS(y,x):
    for k in range(4):
        ny=y+dy[k]
        nx=x+dx[k]
        if 0<=ny<N and 0<=nx<N:
            if chk[ny][nx]==False and mp[ny][nx]==mp[y][x]:
                chk[ny][nx]=True
                DFS(ny,nx)

def RG_DFS(y,x):
    for k in range(4):
        ny=y+dy[k]
        nx=x+dx[k]
        if 0<=ny<N and 0<=nx<N:
            if chk[ny][nx]==False:
                if (mp[x][y]=='R' and mp[nx][ny]=='G') or (mp[x][y]=='G' and mp[nx][ny]=='R') or mp[x][y]==mp[nx][ny]:
                    chk[ny][nx]=True
                    RG_DFS(ny,nx)

cnt=0
for y in range(N):
    for x in range(N):
        if chk[y][x]==False:
            chk[y][x]=True
            DFS(y,x)
            cnt+=1
chk=[[False]*N for _ in range(N)]

rgcnt=0
for y in range(N):
    for x in range(N):
        if chk[y][x]==False:
            chk[y][x]=True
            RG_DFS(y,x)
            rgcnt+=1

print(cnt, end=" ")
print(rgcnt)