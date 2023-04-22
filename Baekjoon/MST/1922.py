# 1. 아이디어
#  - 최소 비용으로 연결 = MST
#  - 인접리스트 생성
#  - heap = (비용, 컴퓨터)
#  - 초기 1번 컴퓨터 heap에 넣고,
#  - 가장 작은 비용 꺼내면서
#  - 방문하지 않은 연결된 다른 컴퓨터들 heap에 넣는다.

# 2. 시간복잡도
#  - MST : O(Elog(E))
#  - Edge=M=100000 >> 가능

# 3. 자료구조
#  - N, M = int
#  - chk = int[]
#  - edge = int[]
#  - res = int

import sys
import heapq # heap
input=sys.stdin.readline

N=int(input())
M=int(input())
edge=[[] for i in range(N+1)]
chk=[False]*(N+1)
res=0

for i in range(M):
    a,b,c=map(int,input().split())
    edge[a].append([c,b])
    edge[b].append([c,a]) # 양방향

# print(edge)
heap=[[0, 1]]

while heap:
    w,node = heapq.heappop(heap)
    if chk[node]==False:
        chk[node]=True
        res+=w
        for next_edge in edge[node]:
            if chk[next_edge[1]]==False:
                heapq.heappush(heap,next_edge) # heap에 추가
                # heappush(저장할 heap, 추가할 edge)
                
print(res)