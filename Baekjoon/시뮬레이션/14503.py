# 1. 아이디어
#  - 특정 조건 만족하는 한 계속 이동 -> while
#  - 4방향 탐색 먼저 수행 -> 빈칸 있을 경우 이동
#  - 4방향 탐색 안될 경우, 뒤로 한 칸 가서 반복
#  - 후진이 불가능하면 종료

# 2. 시간복잡도
#  - While문 최대 : N*M
#  - 각 칸에서 4방향 연산 수행
#  - O(N*M) = 50*50 = 2500 < 2억 >> 가능!

# 3. 자료구조
#  - 전체 지도 : int[][] => 0 : 청소 x, 1 : 벽, 2 : 청소 o
#  - 내 위치, 방향 : int, int, int
#  - 청소한 곳 cnt : int

import sys
input=sys.stdin.readline

N,M=map(int,input().split())
y,x,d=map(int,input().split())
mp=[list(map(int,input().split())) for _ in range(N)]
cnt=0

dy=[-1,0,1,0] # 북, 동, 남, 서
dx=[0,1,0,-1] # <- 반시계 방향

while 1:
    if mp[y][x]==0: # 후진했을 때, 그 칸은 청소되어 있음.
        mp[y][x]=2
        cnt+=1
    sw=False
    for i in range(1,5): # 로봇은 반시게 방향으로 회전하기 때문에 하나씩 줄인다.
        ny=y+dy[(d-i)%4]
        nx=x+dx[(d-i)%4]
        if 0<=ny<N and 0<=nx<M:
            if mp[ny][nx]==0:
                # 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
                d=d-i
                y=ny
                x=nx
                sw=True
                break

    # 4방향 모두 있지 않은 경우
    # switch를 통해 확인
    if sw==False:
        # 뒤쪽 방향이 막혀있는지 확인
        ny=y-dy[d%4]
        nx=x-dx[d%4]
        if 0<=ny<N and 0<=nx<M:
            if mp[ny][nx]==1:
                break
            else:
                y=ny
                x=nx
        else:
            break

print(cnt)