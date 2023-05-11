# 1. 아이디어
#  - 구하고자 하는 값 : 예산들 중 최댓값
#  - 최소 요청액 ~ 최대 요청액 사이값 : 이분 탐색

# 2. 시간복잡도
#  - O(Nlog(N))

import sys
input=sys.stdin.readline

N=int(input())
A=list(map(int,input().split()))
M=int(input())


def half(st,ed):
    # print(st,ed)
    if st>ed:
        print(st-1)
        return

    mid=(st+ed)//2

    s=0
    for i in range(N):
        if A[i]>=mid:
            s+=mid
        else:
            s+=A[i]
    
    if M<s: # 예산액 초과
        half(st,mid-1)
    else: # 같을 때, 포함
        half(mid+1,ed) 

A.sort()
if sum(A)<=M:
    print(A[len(A)-1])
else:
    half(0,A[len(A)-1]) # 왜 0부터 해야되지? 
                        # => 만약, 요청한 예산 모두 같은데, 예산액이 안 되면, 최솟값보다 작게 상한선 걸어야 한다.