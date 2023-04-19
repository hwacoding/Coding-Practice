# 1. 아이디어
#  - X가 3으로 나누어 떨어지면, 3으로 나눈다.
#  - X가 2로 나누어 떨어지면, 2로 나눈다.
#  - 1을 뺀다.

#  - 1, 2, 3번을 구한 값의 칸에서 +1을 하고,
#  - 그 중, 가장 작은 값을 저장한다.

# 2. 시간복잡도
#  - O(N)

# 3. 자료구조
#  - N: int
#  - tmp: int[]
#  - res: int[]

import sys
input=sys.stdin.readline

N=int(input())
res=[0,0,1]

for i in range(3,N+1):
    tmp=[]

    if i%3==0:
        tmp.append(res[i//3]+1)
    if i%2==0:
        tmp.append(res[i//2]+1)

    tmp.append(res[i-1]+1) # 1을 뺀 경우
    
    res.append(min(tmp))

print(res[N])