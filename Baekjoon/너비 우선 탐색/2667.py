
# 1. 아이디어
#  - 2중 for => 값 1 and 방문X ==> DFS
#  - DFS를 통해 찾은 값을 저장 후 정렬해서 출력

# 2. 시간복잡도
#  - BFS : O(V+E)
#  - V : N^2 = 25^2
#  - E : 4*N^2 = 4*25^2
#  - V+E = 5*N^2 ~= N^2 ~= 625 < 2억 >> 가능!

# 3. 자료구조
#  - 그래프 저장 : int[][]
#  - 방문 여부 : bool[][]
#  - 결과값 : int[]

import sys
input=sys.stdin.readline # \n를 읽어오게 된다.

N=int(input())
map=[list(map(int,input().strip()))for _ in range(N)] 
# \n를 int로 변환할 수 없기에 \n 제거를 위해 strip()을 사용
# strip은 공백 제거된 원래 문자열을 반환
# 원래 문자열 list 변환 시, '1','2','3'...

# split()은 공백을 기준으로 input 인지
# 이어진 입력은 하나로 인지
# list 변환 시, '123'
chk=[[False] * N for _ in range(N)]
result=[]
each=0

dy=[0,1,0,-1]
dx=[1,0,-1,0]

def dfs(y,x):
    global each
    each+=1
    for k in range(4):
        ny=y+dy[k]
        nx=x+dx[k]
        if 0<=ny<N and 0<=nx<N:
            if map[ny][nx]==1 and chk[ny][nx]==False:
                chk[ny][nx]=True
                dfs(ny,nx) # 방문한 곳은 가지 않기 때문에 이어진 집을 찾는다.

for i in range(N):
    for j in range(N):
        if map[i][j]==1 and chk[i][j]==False:
            # 방문 체크 표시
            chk[i][j]=True
            # DFS로 크기 구하기
            each=0
            dfs(i,j)
            result.append(each)
            # 구한 크기 결과 리스트에 넣기

result.sort()
print(len(result))
for i in result:
    print(i)