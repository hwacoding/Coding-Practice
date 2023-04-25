# 1. 아이디어
#  - 한 점에서 다른 점까지 가는 최소비용 : 다익스트라
#  - 거리 배열 초기화, 시작점 0
#  - (비용, 시작점) heap에 넣고 시작
#  - 출발점에서 비용 더한 값이 도착점 거리보다 작으면 갱신

# 2. 시간복잡도
#  - 다익스트라 : O(Elog(V))
#  - E = 100,000
#  - V = 1000

# 3. 자료구조
#  - N, M : int
#  - edge : (w, v) []
#  - dist = int[]

import sys
import heapq
input=sys.stdin.readline
INF=sys.maxsize

N=int(input())
M=int(input())
edge=[[] for _ in range(N+1)]
dist=[INF]*(N+1)

for i in range(M):
    u,v,w=map(int,input().split())
    edge[u].append([w,v])

st,en=map(int,input().split())

dist[st]=0
heap=[[0,st]]

while heap:
    # print(heap)
    ew,ev=heapq.heappop(heap) # ev까지 왔을 때의 총 비용 값 = ew
    # print(dist[ev],ew)
    if dist[ev]<ew: continue 
    # --★ 여러 경로를 통해 오게 된 현재 위치까지의 거리가 이미 구해둔 거리보다 짧으면, for문 넘어간다. ★--
    for nw,nv in edge[ev]:
        if dist[ev]+nw<dist[nv]:
            dist[nv]=dist[ev]+nw
            heapq.heappush(heap,[dist[nv],nv]) # 갱신한 거리, 위치 heap에 넣기

print(dist[en])

    