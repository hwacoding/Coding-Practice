# 1. 아이디어
#  - bfs
#  - 4방향 익지 않은 토마토이면, Queue에 저장
#  - Queue에서 하나씩 빼고, 4방향 확인 -> 반복
#  - 토마토가 모두 익지 못하는 상황 체크 
#  - 시간 다 지나고, 맵에서 익지 않은 토마토 있는지 확인

# 2. 시간복잡도
#  - O(V+E) = O(5*V) = 5,000,000 >> 가능
#  - 처음 익은 토마토 찾기 : O(V)
#  - 토마토 모두 익지 못하는 상황 = O(V)
#  - 결과적으로 O(7*V) = 7,000,000 >> 가능!

# 3. 자료구조
#  - N,M : int
#  - mp : int[][]
#  - st : int[]
#  - Queue : int[]
 
import sys
from collections import deque
# --★ deque 모듈 안쓰면 시간복잡도 박살남(pop(0)이 시간복잡도가 O(n)이고 popleft()가 O(1)이라고 함) ★--

input=sys.stdin.readline
M,N=map(int,input().split())
mp=[]

for i in range(N):
    tmp=list(map(int,input().split()))
    mp.append(tmp)

dy=[0,1,0,-1]
dx=[1,0,-1,0]

q=deque([])

def bfs():
    while q:
        y,x=q.popleft()
        for k in range(4):
            ny=y+dy[k]
            nx=x+dx[k]
            if 0<=ny<N and 0<=nx<M:
                if mp[ny][nx]==0:
                    mp[ny][nx]=mp[y][x]+1 # 익은 날짜를 저장한다.
                    q.append((ny,nx))
                

# 1. 시작점 찾기
# O(N*M)
for i in range(N):
    for j in range(M):
        if mp[i][j]==1:
            q.append((i,j))

bfs()

sw=False
res=0
for i in range(N):
    for j in range(M):
        if mp[i][j]==0:
            print(-1)
            sw=False
            break
        else:
            res=max(res,mp[i][j])
            sw=True
    if sw==False:
        break

if sw==True:
    print(res-1)

# for i in mp:
#     print(i)