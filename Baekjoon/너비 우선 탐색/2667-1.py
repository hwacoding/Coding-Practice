# 1. 아이디어
#  - BFS(y,x)
#  - 방문한 곳이 아니고, 0이 아니면, cnt+=1
#  - 결과값 배열에 저장 후 sort

# 2. 시간복잡도
#  - O(V+E)
#  - V=N^2
#  - E=4*V
#  - O(4V)~=O(N^2)=25^2 < 2억 >> 가능!

# 3. 자료구조
#  - mp : int[][]
#  - chk : int[][]
#  - res : int[]

import sys
input=sys.stdin.readline

N=int(input())
mp=[list(map(int,input().strip())) for _ in range(N)]
chk=[[False]*N for _ in range(N)]

dy=[1,0,-1,0]
dx=[0,1,0,-1]
cnt=0

def bfs(y,x):
    global cnt
    for k in range(4):
        ny=y+dy[k]
        nx=x+dx[k]
        if 0<=ny<N and 0<=nx<N:
            if mp[ny][nx]==1 and chk[ny][nx]==False:
                chk[ny][nx]=True
                bfs(ny,nx)
                cnt+=1

# print(chk)
res=[]
for i in range(N):
    for j in range(N):
        if mp[i][j]==1 and chk[i][j]==False:
            chk[i][j]=True
            cnt+=1
            bfs(i,j)
            res.append(cnt)
            cnt=0

res.sort()
print(len(res))
for i in res:
    print(i)