# 1. 아이디어
#  - 정확하게 만들 수 없으면, -1 => 그리디 알고리즘
#  - 5kg 하나씩 증가.
#  - (Nkg - 5kg*nums) % 3 ==0 : 3kg 개수 구함
#  - 최솟값 갱신

# 2. 시간복잡도
#  - O(N)

# 3. 자료구조
#  - N : int
#  - cnt : int

import sys
input=sys.stdin.readline

N=int(input())
bags=[5,3]
a=0
b=0
res=N

for i in range(0,N//5+1):
    if(N-5*i)%3==0:
        a=i
        b=(N-5*a)//3
        # print(a,b)
        res=min(a+b,res)

if res==N:
    print(-1)
else:
    print(a+b)