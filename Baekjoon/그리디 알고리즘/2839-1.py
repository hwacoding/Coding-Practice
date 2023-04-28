# 1. 아이디어
#  - 3kg, 5kg
#  - 5kg 최대로 넣고, 3kg 넣을 수 있는지 확인
#  - 안되면, 5kg 개수 하나씩 줄이면서 확인
#  - 그리디 알고리즘

# 2. 시간복잡도
#  - O(N)

# 3. 자료구조
#  - N : int

import sys
input=sys.stdin.readline

N=int(input())

a=N//5

sw=False
while a>=0:
    b=N-5*a # 나머지
    if b%3==0:
        c=b//3
        print(a+c)
        sw=True
        break
    else:
        a-=1

if sw==False:
    print(-1)