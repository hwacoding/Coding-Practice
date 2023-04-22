# 1. 아이디어
#  - MST 기본문제, 외우기
#  - 간선을 인접리스트에 집어넣기
#  - 힙에 시작점 넣기
#  - 힙이 빌 때까지 다음의 작업을 반복
#         - 힙의 최솟값 꺼내서, 해당 노드 방문 안했다면,
#                 - 방문표시, 해당 비용 추가, 연결된 간선을 힙에 넣어주기

# 2. 시간복잡도
#  - MST : O(Edge*log(Edge))

# 3. 자료구조
#  - 간선 저장 되는 인접리스트 : (무게, 노드번호)
#  - 힙 : (무게, 노드번호)
#  - 방문 여부 : bool[]
#  - MST 결과값 : int

import sys
import heapq # heap 자료구조
input=sys.stdin.readline

V,E=map(int,input().split())
edge=[[] for _ in range(V+1)]
chk=[False]*(V+1)
res=0

for i in range(E):
    a,b,c=map(int,input().split())
    edge[a].append([c,b])
    edge[b].append([c,a]) # 양방향 그래프

heap=[[0,1]] # 시작점 먼저 넣어줌

while heap:
    w, each_node = heapq.heappop(heap) # w 최솟값 노드 꺼내기

    if chk[each_node]==False:
        chk[each_node]=True
        res+=w
        for next_edge in edge[each_node]: # 꺼낸 노드의 간선들 중 방문 안한 노드를 heap에 추가
            if chk[next_edge[1]]==False:
                heapq.heappush(heap,next_edge)

print(res)