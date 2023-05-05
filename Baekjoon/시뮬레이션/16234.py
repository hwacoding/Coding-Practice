# 1. 아이디어
#  - BFS
#  - 방문 체크

# 2. 시간복잡도
#  - O(2000*(V+E))
#  - E=V^2=2500
#  - 5,000,000 >> 가능

import sys
from collections import deque
input=sys.stdin.readline

N,L,R=map(int,input().split())
mp=[list(map(int,input().split())) for _ in range(N)]
chk=[[False]*N for _ in range(N)]
Q=deque([])
tmp=[]

dy=[0,1,0,-1]
dx=[1,0,-1,0]

def bfs(y,x):
    Q.append((y,x))
    tmp.append((y,x)) # 연합 저장

    while Q:
        # print(tmp)
        # print(chk)
        ey,ex=Q.popleft()

        for k in range(4):
            ny=ey+dy[k]
            nx=ex+dx[k]
            if 0<=ny<N and 0<=nx<N and chk[ny][nx]==False:
                if L<=abs(mp[ey][ex]-mp[ny][nx])<=R:
                    chk[ny][nx]=True
                    Q.append((ny,nx))
                    tmp.append((ny,nx))

sw=False
res=0
while 1:
    for y in range(N):
        for x in range(N):
            if chk[y][x]==False:
                chk[y][x]=True
                bfs(y,x)
            
            if len(tmp)>1: # 연합이 있으면,
                # print(tmp)
                sw=True
                s=0
                for cx,cy in tmp:
                    s+=mp[cx][cy]
                s=s//len(tmp)

                for cx,cy in tmp: # 인구수 수정
                    mp[cx][cy]=s

            tmp=[]

    if sw==False: # 연합할 수 있는 땅이 없으면, 끝
        break
    else:
        chk=[[False]*N for _ in range(N)]
        res+=1 # 인구 이동 날짜 추가
    sw=False

# print(mp)
print(res)