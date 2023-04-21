# 1. 아이디어
#  - 잡아 먹을 수 있는 물고기 위치 저장.
#  - BFS를 통해 물고기까지의 거리 저장.
#  - 가장 가까운 물고기 많으면, 그 중 맨 위에 있는 물고기 먹으러 간다.
#  - 맨 위에 있는 물고기가 많으면, 왼쪽 먹는다.
#  - 크기만큼 먹으면 크기가 1 증가 => 다시 잡아 먹을 수 있는 물고기 저장.

# 2. 시간복잡도
#  - 먹을 수 있는 물고기 거리 구하기 : BFS : O(V+E) = O(5*V) = O(5*N^2)
#  - 거리 sort : O(N)
#  - 총 O(N^3) : N = 20 >> 가능!

# 3. 자료구조
#  - mp : int[][]
#  - fish : int[]
#  - dis : int[]

import sys
from collections import deque
input=sys.stdin.readline

N=int(input())
mp=[list(map(int,input().split())) for _ in range(N)]
size=2
y,x=0,0

fish=[]

dy=[0,1,0,-1]
dx=[1,0,-1,0]
Q=deque()

def bfs():
    dist=0
    while Q:
        L=len(Q)
        for i in range(L):
            y,x=Q.popleft()
            for k in range(4):
                ny=y+dy[k]
                nx=x+dx[k]
                if 0<=ny<N and 0<=nx<N:
                    # 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.
                    if chk[ny][nx]==False:
                        chk[ny][nx]=True
                        if mp[ny][nx]==0 or mp[ny][nx]==size:
                            Q.append((ny,nx))
                        elif 0<mp[ny][nx]<size:
                            fish.append((ny,nx,dist))
        dist+=1
        # print(chk)
        # print(Q)

# 물고기 현재 위치
for i in range(N):
    for j in range(N):
        if mp[i][j]==9:
            y=i
            x=j
Q.append((y,x))

t=0
eat=0

while 1:
    chk=[[False]*N for _ in range(N)]
    chk[y][x]=True
    Q.append((y,x))
    # 먹을 수 있는 물고기 거리 배열 제작
    bfs()
    # 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
    if len(fish)==0:
        print(t)
        break
    # 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
    else:
        # 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
        fish.sort(key=lambda x:(x[2],x[0],x[1]))
        mp[y][x]=0
        y,x=fish[0][0],fish[0][1]
        mp[y][x]=9
        t+=fish[0][2]+1
        eat+=1

        if eat==size:
            size+=1
            eat=0

        fish=[]

    # print(mp)
