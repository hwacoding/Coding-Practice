# 1. 아이디어
#  - while
#  - 현재 프린트할 문서 가리키는 idx의 값이 max값보다 작으면, idx+=1
#  - max값이면, 프린트 => cnt+=1
#  - M번째 문서 출력되면, 종료 -> break

# 2. 시간복잡도
#  - O(N*N) = 100*100 (max, N for문) < 2억 >> 가능!

# 3. 자료구조
#  - idx : int
#  - max : int

import sys
input=sys.stdin.readline

C=int(input())
mx=0

for i in range(C):
    N,M=map(int,input().split())
    q=list(map(int,input().split()))
    cnt=1

    mx=max(q)
    idx=0
    while 1:
        if q[idx]==mx and idx==M: # 현재 출력하는 문서의 중요도가 1등이고, M번째 문서면 break
            break
        
        if q[idx]==mx:
            q.pop(idx)
            if idx<M: # M이 프린트한 문서보다 뒤에 있을 경우
                M-=1 # 한 칸 앞으로 온다.
            if idx>=len(q): # 맨 마지막 문서일 경우
                idx=0
            mx=max(q)
            cnt+=1
        else:
            idx+=1
            idx=idx%len(q)

    print(cnt)