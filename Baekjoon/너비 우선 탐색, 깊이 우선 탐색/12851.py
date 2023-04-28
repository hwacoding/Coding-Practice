# 1. 아이디어
#  - 순간이동, 앞, 뒤
#  - BFS
#  - 방문한 곳은 안 간다.
#  - cnt 같이 저장

# 2. 시간복잡도
#  - O(N)

# 3. 자료구조
#  - N,K : int
#  - cnt = 방문 횟수 체크 : int[]
#  - chk : int[]

import sys
from collections import deque
input=sys.stdin.readline

N,K = map(int,input().split())
chk=[False]*100001
Q=deque([])
res=0

def bfs(st,en):
    global res
    Q.append(st)
    chk[st]=True
    
    while Q: 
        # Q에 저장하는 단계에서 동생을 찾을 수 있는 방법의 수를 찾아야 하므로
        # 다 저장한 후에 chk를 한다.
        if en in Q: # Queue에 도착점 있는지 확인
            return Q.count(en) # 있으면, 카운트
        
        for i in range(len(Q)): # 갈 수 있는 모든 곳을 Queue에 저장 후,
            p=Q.popleft()

            if 2*p<len(chk) and chk[2*p]==False:
                Q.append(2*p)
            if p+1<len(chk) and chk[p+1]==False:
                Q.append(p+1)
            if p-1>=0 and chk[p-1]==False:
                Q.append(p-1)
        res+=1
        # print(Q)

        
        for p in Q: # check한다.
            chk[p]=True
        

ck=bfs(N,K)

print(res)
print(ck)
# print(cnt[K])
