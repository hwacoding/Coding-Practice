# 1. 아이디어
#  - 주어진 동전이 배수이기 때문에 그리디 알고리즘
#  - 가장 큰 거 먼저 채우면 된다.

# 2. 시간복잡도
#  - O(N!) => N 최대 10

import sys
input=sys.stdin.readline

N,K=map(int,input().split())
A=[int(input()) for _ in range(N)]
A.reverse()
# print(A)
res=0

while 1:
    if K==0:
        break

    for i in range(N):
        if K>=A[i]:
            break

    res+=K//A[i]
    K=K%A[i]

print(res)