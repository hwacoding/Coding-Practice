# 1. 아이디어
#  - 규칙
#  - A(n)=A(n-1)+A(n-2)

# 2. 시간복잡도
#  - O(N)

import sys
input=sys.stdin.readline

n=int(input())
A=[0,1,2,3]

if n<=3:
    print(A[n])
else:
    k=3
    while 1:
        A.append(A[k-1]+A[k])       
        k+=1

        if n==k:
            print(A[k]%10007)
            break
            