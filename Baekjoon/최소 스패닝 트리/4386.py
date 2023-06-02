# 1. 아이디어
#  - MST
#  - 별자리 비용을 구한다.
#  - heap에 첫 번째 별자리 넣고,
#  - heap에서 하나씩 빼면서, 방문하지 않았으면 heap에 추가
#  - heap에서 최솟값을 빼기 때문에 그렇게 이으면, 최소!

# 2. 시간복잡도
#  - O(N^2) : 별자리 비용
#  - O(Elog(E)) : MST

import sys
import math
import heapq
input=sys.stdin.readline

n=int(input())
Star=[list(map(float,input().split())) for _ in range(n)]
edge=[[] for _ in range(n)]
chk=[False]*n

for i in range(n):
    for j in range(i+1,n):
        edge[i].append([math.sqrt((Star[i][0]-Star[j][0])**2+(Star[i][1]-Star[j][1])**2),j])
        edge[j].append([math.sqrt((Star[i][0]-Star[j][0])**2+(Star[i][1]-Star[j][1])**2),i])

heap=[[0,0]]
res=0
while heap:
    ew, ev=heapq.heappop(heap)

    if chk[ev]==False:
        chk[ev]=True
        res+=ew
        for nw,nv in edge[ev]:
            if chk[nv]==False:
                heapq.heappush(heap,[nw,nv])

print(round(res,2))