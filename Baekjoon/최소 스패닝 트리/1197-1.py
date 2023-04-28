# 1. 아이디어
#  - 최소 스패닝 트리 : MST
#  - 연결 가능한 최소 간선 꺼내기 : heap
#  - 연결 안 되어있으면 연결

# 2. 시간복잡도
#  - 모든 간선 확인
#  - heap에서 최소 꺼냄
#  - O(Elog(E))

# 3. 자료구조
#  - V,E=int
#  - chk=int[]
#  - edge=[비용, 연결 노드]

import sys
import heapq
input=sys.stdin.readline

V,E=map(int,input().split())
edge=[[] for _ in range(V+1)]
chk=[False]*(V+1)

for i in range(E):
    u,v,w=map(int,input().split())
    edge[u].append([w,v])
    edge[v].append([w,u])

heap=[[0,1]] # 1번 노드부터 시작
res=0

while heap:
    ew,ev=heapq.heappop(heap) # 방문할 노드와 비용
    
    if chk[ev]==False:
        chk[ev]=True
        res+=ew

        for nw,nv in edge[ev]:
            if chk[nv]==False:
                heapq.heappush(heap,[nw,nv])

print(res)