# 1. 아이디어
#  - 이 방법보다 더 필요한 시간의 합을 최소로 만들 수는 없다. => 그리디
#  - sort 후, N-i를 곱하면 된다.

# 2. 시간복잡도
#  - sort : O(Nlog(N))
#  - O(N)

# 3. 자료구조
#  - N : int
#  - times : int[]

import sys
input=sys.stdin.readline

N=int(input())
times=list(map(int,input().split()))

times.sort()
res=0
for i in range(N):
    res+=times[i]*(N-i)
print(res)