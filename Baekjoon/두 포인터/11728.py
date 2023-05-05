# 1. 아이디어

# 2. 시간복잡도
#  -O(2*N*log(2*N)) = 2*백만*20= 4천만 => A,B 합친 후, 정렬
#  -O(2*N*log(N)+N) = 2천만+백만 => A, B 따로 정렬 후, 합침

import sys
input=sys.stdin.readline

n,m=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

C=A+B
C.sort()

for i in C:
    print(i, end=" ")