n=int(input())
visited=[[0 for i in range(n)] for j in range(n)] ## 방문한 노드 표시
S=[]

for i in range(n):
    s=input()
    S.append(s)

cnt=0
def DFS(y,x):
    global cnt
    global visited

    if x<0 or y<0 or x>=n or y>=n or S[y][x]=='0' or visited[y][x]==1: ## 1. 범위 밖
                                                                       ## 2. 장애물 없거나
                                                                       ## 3. 방문한 곳이면, return
        return
    else:
        visited[y][x]=1
        cnt+=1
        # print(y,x)
        DFS(y,x-1)
        DFS(y,x+1)
        DFS(y-1,x)
        DFS(y+1,x)
        

        return cnt
        
block_cnt=0
C=[]
for i in range(n):
    for j in range(n):
        if S[i][j]=='1' and visited[i][j]==0:
            DFS(i,j)
            C.append(cnt)
            block_cnt+=1
            cnt=0

print(block_cnt)
C.sort()

for i in range(len(C)):
    print(C[i])