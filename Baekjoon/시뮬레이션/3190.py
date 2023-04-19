# 1. 아이디어
#  - 시뮬레이션
#  - 초기 y,x = 0,0, 오른쪽
#  - 시간 기준으로 진행
#  - 다음 칸 미리 보고, 벽이거나 자신의 몸이면 끝.

# 2. 시간복잡도
#  - O(N^2) = 10000 >> 가능

# 3. 자료구조
#  - mp : int[][]     사과 : 1, 자신 : 2
#  - ro : 회전

import sys
input=sys.stdin.readline

N=int(input())
K=int(input())
mp=[[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(K):
    y,x=map(int,input().split())
    mp[y][x]=1
mp[1][1]=2 # 초기 자신 위치

# --★ 맵 상의 행과 열의 index 주의!!! ★---
# 현재 첫 번째가 (1,1)

L=int(input())
d=[]
for i in range(L):
    X,C=input().split()
    d.append((int(X),C))

# print(d)

s=[(1,1)] # y, x

dy=[0,1,0,-1]
dx=[1,0,-1,0]
idx=0
t=0

# for i in mp:
#     print(i)

while 1:
    t+=1

    y=s[len(s)-1][0] # 뱀 머리 좌표
    x=s[len(s)-1][1]

    ny=y+dy[idx]
    nx=x+dx[idx]
    if 1<=ny<N+1 and 1<=nx<N+1:
        #만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
        if mp[ny][nx]==1:
            mp[ny][nx]=2
            s.append((ny,nx))

            y=ny
            x=nx
        #만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
        elif mp[ny][nx]==0:
            mp[ny][nx]=2
            s.append((ny,nx))
            # 뱀 이동
            ty,tx=s.pop(0)
            mp[ty][tx]=0

            y=ny
            x=nx
        # 자신이 몸에 부딪히는 경우
        else:
            break

    else:
        # 벽에 부딪히는 경우
        break

    # 방향 회전
    if len(d)!=0 and d[0][0]==t:
        if d[0][1]=='D':
            idx=(idx+1)%4
        else:
            idx=(idx-1)%4
        d.pop(0)
    
    # print('t: ',t)
    # for i in mp:
    #     print(i)
    # print(idx)    
    # print("s : ",s)

print(t)