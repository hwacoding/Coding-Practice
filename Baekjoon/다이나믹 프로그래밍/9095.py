# 1. 아이디어
#  - 점화식 : A(n)=A(n-1)+A(n-2)+A(n-3)

# 2. 시간복잡도
#  - O(N)

# 3. 자료구조
#  - T : int
#  - nums : int[]
#  - res : int[]
#  - max : int

import sys
input=sys.stdin.readline

T=int(input())
nums=[int(input()) for _ in range(T)]
m=max(nums)
res=[0,1,2,4]

for i in range(4,m+1):
    res.append(res[i-1]+res[i-2]+res[i-3])

for num in nums:
    print(res[num])