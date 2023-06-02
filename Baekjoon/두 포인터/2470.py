# 1. 아이디어
#  - 두 포인터
#  - 정렬 후, 결과값이 0보다 크면, 오른쪽 -1
#  - 결과값이 0보다 작으면, 왼쪽 +1

# 2. 시간복잡도
#  - O(2N)

import sys
MAX_SIZE=sys.maxsize
input=sys.stdin.readline

N=int(input())
A=list(map(int,input().split()))

A.sort()
left=0
right=len(A)-1
res=MAX_SIZE

resL=A[left]
resR=A[right]

while 1:
    if left==right:
        break

    tmp=A[left]+A[right]
    # print(A[left],A[right],res)

    if abs(res)>abs(tmp):
        res=tmp
        resL=A[left]
        resR=A[right]
        # print(resL, resR)
    
    if tmp<0:
        left+=1
    elif tmp>0:
        right-=1
    else:
        break

print(resL,resR)