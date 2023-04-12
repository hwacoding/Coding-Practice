
# 1. 아이디어
#  - 2중 for => 값 1 and 방문X ==> BFS
#  - BFS 돌면서 그림 개수 +1, 최대값을 갱신

# 2. 시간복잡도
#  - BFS : O(V+E)
#  - V : m*n = 500*500
#  - E : V*4 = 500*500*4
#  - V+E = 5*250000 = 100만 < 2억 >> 가능!

# 3. 자료구조
#  - 그래프 전체 지도 : int[][]
#  - 방문 : bool[][]
#  - Queue(BFS)

import sys
input = sys.stdin.readline # 입출력 속도 빠르게

n,m=map(int,input().split())
map=[list(map(int,input().split())) for _ in range(n)]
chk=[[False]*m for _ in range(n)]

dy=[0,1,0,-1] # 오른쪽, 아래, 왼쪽, 위
dx=[1,0,-1,0] 

def bfs(y,x):
    rs=1 # return할 그림 크기
    q=[(y,x)]
    while q: # q가 새로 더이상 들어가지 않을 때까지
        ey,ex=q.pop()
        for i in range(4):
            ny=ey+dy[i]
            nx=ex+dx[i]
            if 0<=ny<n and 0<=nx<m: # 범위 넘어가면 안된다.
                if map[ny][nx]==1 and chk[ny][nx]==False:
                    rs+=1
                    chk[ny][nx]=True
                    # 파이썬 리스트는 리스트 원소들의 포인터를 저장하고 있기에 전역변수 설정 안해도 된다.
                    # 변수는 해줘야 한다.
                    q.append((ny,nx))

    return rs


cnt=0
maxv=0
for i in range(n):
    for j in range(m):
        if map[i][j]==1 and chk[i][j]==False:
            # 방문했음
            chk[i][j]=True
            # 전체 그림 갯수를 +1
            cnt+=1
            # BFS > 그림 크기를 구해주고
            # 최대값 갱신
            maxv=max(maxv,bfs(i,j))

print(cnt)
print(maxv)