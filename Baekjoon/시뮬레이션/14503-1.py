# 1. 아이디어
#  - 시뮬레이션
#  - 로봇은 계속 진행. 재귀함수x => while
#  - 청소 x -> 청소 -> 주변 4칸 확인 

# 2. 시간복잡도
#  - O(N*M)

# 3. 자료구조
#  - mp=[][] 청소x : 0, 벽 : 1, 청소o : 2
#  - y,x,d : int
#  - cnt : int

import sys
input=sys.stdin.readline

N,M=map(int,input().split())
y,x,d=map(int,input().split())
mp=[list(map(int,input().split())) for _ in range(N)]

dy=[-1,0,1,0] # 북,동,남,서
dx=[0,1,0,-1]

cnt=0

while 1:
    # 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    if mp[y][x]==0:
        mp[y][x]=2        
        cnt+=1

    sw=False

    for k in range(1,5):
        ny=y+dy[(d-k)%4] # 반시계
        nx=x+dx[(d-k)%4]
        if 0<=ny<N and 0<=nx<M:
            if mp[ny][nx]==0:
                # 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
                d=(d-k)%4 # 반시계 방향으로 회전
                y=ny
                x=nx
                sw=True
                break
    # 4칸 모두 확인 완료

    # 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    if sw==False:
        ny=y-dy[d]
        nx=x-dx[d]
        #. 후진 할 수 있으면, 후진하고 1번으로
        if 0<=ny<N and 0<nx<=M:
            if mp[ny][nx]==1: # 후진할 수 없는 경우
                break
            else:
                y=ny # 후진할 수 있는 경우
                x=nx 
        else:
            break


print(cnt)