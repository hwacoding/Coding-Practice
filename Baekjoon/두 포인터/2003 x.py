# 1. 아이디어
#  - 2중 for문
#  - i 번째를 기준으로 M-i
#  - M-i가 0이 되면, cnt+=1
#  - M-i가 0보다 작으면, break -> i+=1

#  - 0번째 기준으로 먼저 값 더함
#  - 앞, 뒤 포인터
#  - 더한 값이 크면, 앞에꺼 뺌
#  - 작으면, 뒤에꺼 더함

# 2. 시간복잡도
#  - N+(N-1)+... = 50,000,000 < 2억 >> 가능! : 시간 제한 0.5초 >> 불가능

#  - O(N)+O(N)+O(N) ~= O(N) >> 가능!

# 3. 자료구조
#  - N, M : int
#  - 배열 : int[]
#  - tmp : int

#  - f, b: int

import sys
input=sys.stdin.readline

N,M=map(int,input().split())
A=list(map(int,input().split()))
cnt=0
f=0 # 앞 포인터
b=0 # 뒤 포인터
tmp=0

# for i in range(N): # 0번째 기준으로 값 구함
#     tmp+=A[i]
    
#     if tmp>=M:
#         b=i+1
#         break

while 1:
    if f==len(A):
        break

    # if tmp>=M:
    #     tmp-=A[f]
    #     f+=1
    if tmp<M and b!=len(A):
        tmp+=A[b]
        b+=1
    else: # tmp가 작고, b는 끝까지 간 상황
        tmp-=A[f]
        f+=1
    #   ---★ 모든 상황 고려하여 확실하게 처리해야 한다! ★---

    if tmp==M:
        # print(f)
        cnt+=1


print(cnt)