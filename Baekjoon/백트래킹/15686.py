# 1. 아이디어
#  - 치킨집 선택 : 백트래킹
#  - 집마다 치킨거리 구함 : BFS

# 2. 시간복잡도
#  - 백트래킹 : 2^13
#  - O((V+E)*2^13)
 
import sys
from collections import deque
MAX_SIZE=sys.maxsize
input=sys.stdin.readline

N,M=map(int,input().split())
mp=[list(map(int,input().split())) for _ in range(N)]
chk=[[False]*N for _ in range(N)]

BBQ=[]
CBBQ=[]

dy=[0,1,0,-1]
dx=[1,0,-1,0]
dis=0 # 치킨 거리
Q=deque()

tmp=0
res=MAX_SIZE

def BFS():
    global dis
    global tmp
    # Q에 치킨 집 들어가 있음.
    
    while Q:
        # print(Q)
        ql=len(Q)
        dis+=1
        for i in range(ql):
            ey,ex=Q.popleft()
            for k in range(4):
                ny=ey+dy[k]
                nx=ex+dx[k]
                if 0<=ny<N and 0<=nx<N:
                    if chk[ny][nx]==False:
                        chk[ny][nx]=True
                        Q.append((ny,nx))
                        if mp[ny][nx]==1:
                            tmp+=dis
# BFS 안하고, 집들까지와의 거리를 구해도 된다. => 더 빠름.


def recur(st,lev):
    global dis
    global tmp
    global res
    global chk

    if lev==0:
        # print(CBBQ)
        for y,x in CBBQ:
            Q.append((y,x))
            chk[y][x]=True # 정한 치킨집 True
        
        BFS()
        
        if res>tmp:
            res=tmp
        tmp=0
        dis=0
        chk=[[False]*N for _ in range(N)]

        return
    
    for i in range(st,len(BBQ)):
        CBBQ.append(BBQ[i])
        recur(i+1,lev-1)
        CBBQ.pop()

for i in range(N):
    for j in range(N):
        if mp[i][j]==2:
            BBQ.append((i,j))

recur(0,M)

print(res)