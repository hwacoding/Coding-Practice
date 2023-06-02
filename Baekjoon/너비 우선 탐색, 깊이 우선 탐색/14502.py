# 1. 아이디어
#  - 3개 둘 곳 순열 생성
#  - 바이러스 확산 : BFS
#  - 안전 영역 최대 갱신

# 2. 시간복잡도
#  - O(64*63*62) = 3600*60 = 216000
#  - O(V+E) = 64+256 = 300
#  - O(N*M) = 64 : chk 초기화
#  - 420,000,000 >> 제한시간 2초 => 가능

import sys
from collections import deque
input=sys.stdin.readline

N,M=map(int,input().split())
mp=[list(map(int,input().split())) for _ in range(N)]
res=0

dy=[0,1,0,-1]
dx=[1,0,-1,0]
def BFS():
    global res
    chk=[[False]*M for _ in range(N)]
    Q=deque()

    for y in range(N):
        for x in range(M):
            if mp[y][x]==2:
                Q.append((y,x))
                chk[y][x]=True
            elif mp[y][x]==1:
                chk[y][x]=True

    while Q:
        ey,ex=Q.popleft()

        for k in range(4):
            ny=ey+dy[k]
            nx=ex+dx[k]
            if 0<=ny<N and 0<=nx<M:
                if mp[ny][nx]==0 and chk[ny][nx]==False:
                    chk[ny][nx]=True
                    Q.append((ny,nx))

    cnt=0

    for y in range(N):
        for x in range(M):
            if chk[y][x]==False:
                cnt+=1

    if res<cnt:
        res=cnt

af=0
bf=0
cf=0

for a in range(N*M):
    ay=a//M
    ax=a%M
    if mp[ay][ax]==0:
        mp[ay][ax]=1
        af=1
        for b in range(a,N*M):
            by=b//M
            bx=b%M
            if mp[by][bx]==0:
                mp[by][bx]=1
                bf=1
                for c in range(b,N*M):
                    cy=c//M
                    cx=c%M
                    if mp[cy][cx]==0:
                        mp[cy][cx]=1
                        cf=1
                        # a,b,c 위치에 벽 세웠음
                        # BFS로 감염 시작
                        # for L in mp:
                        #     print(L)
                        # print('==============================')

                        BFS()
                        # print(res)
                    if cf==1: # 벽 설치했었으면,
                        mp[cy][cx]=0 # 원상 복구
                        cf=0
            if bf==1:
                mp[by][bx]=0
                bf=0
    if af==1:
        mp[ay][ax]=0
        af=0

print(res)