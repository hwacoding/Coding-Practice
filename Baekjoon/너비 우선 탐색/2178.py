# 1. 아이디어
#   - 이중 for문 => 1 and 방문한 칸 X => n,m 나올 때까지 res+=1
#   - BFS => 최소의 칸 수
#   - 단계적으로 Queue에 쌓여있는 것들을 처리

# 2. 시간복잡도
#   - O(V+E)
#   - V = N*M
#   - E = 4*V
#   - V+E = 5*V = 5*N*M = 50,000 < 2억 ==> 가능!

# 3. 자료구조
#   - mp = int[][]
#   - chk = int[][]
#   - Queue : BFS
~
import sys
input=sys.stdin.readline

N,M=map(int,input().split())
mp=[list(map(int,input().strip())) for _ in range(N)]
chk=[[False]*M for _ in range(N)]
chk[0][0]=True

dy=[1,0,-1,0]
dx=[0,1,0,-1]

def bfs():
    while q1:    
        # print(q1)
        y=q1[0][0]
        x=q1[0][1]
        del q1[0]

        for k in range(4):
            ny=y+dy[k]
            nx=x+dx[k]
            if 0<=ny<N and 0<=nx<M:
                if mp[ny][nx]==1 and chk[ny][nx]==False:
                    chk[ny][nx]=True
                    q2.append((ny,nx)) # 다음 단계 Queue에 저장

sy=0
sx=0
res=1
cnt=0

q1=[(sy,sx)] # 현재 단계
q2=[] # 다음 단계
while 1:
    if (N-1,M-1) in q1: # 도달
        break

    bfs() # 단계적으로 Queue에 쌓인 모든 칸들을 방문
    q1=q2.copy()
    q2=[]
    res+=1

print(res)