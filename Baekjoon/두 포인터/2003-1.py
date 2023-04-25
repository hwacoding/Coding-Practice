# 1. 아이디어
#  - 연속된 합 : 두 포인터
#  - left, right = 0 에서 시작
#  - 작으면, right+=1
#  - 크면, left+=1
#  - 다 돌기 위해서는 left가 끝까지 갈 때, break

# 2. 시간복잡도
#  - O(N)
#  - N : 1만

# 3. 자료구조
#  - N,M : int
#  - Arr : int[]
#  - left, right : int

import sys
input=sys.stdin.readline

N,M = map(int,input().split())
Arr=list(map(int,input().split()))

left=0
right=0
sum=0
res=0

while 1:
    if left==N:
        break

    if sum<M and right<N: # 작을 경우
        sum+=Arr[right]
        right+=1  
    else: # 크거나 sum 값을 증가할 수 없는 경우
        sum-=Arr[left]
        left+=1

    if sum==M:
        # print(left,right)
        res+=1    

print(res)
