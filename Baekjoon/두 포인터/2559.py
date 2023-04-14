# 1. 아이디어
#  - 첫 번째
#  - for문으로 각 숫자의 위치에서 이후 k개의 수 더함
#  - 이때마다 최대값으로 갱신

#  - 두 번째
#  - 처음 k개의 값을 구함
#  - for 문: 다음 인덱스의 값을 더하고, 앞의 값을 뺌
#  - 이때 최대값을 갱신

# 2. 시간복잡도
#  - 첫 번째
#  - O(n*k)
#  - n*k=10^10 > 2억 >> 불가능

#  - 두 번째
#  - O(2*N) ~= O(N)

# 3. 자료구조
#  - 전체 정수 배열 : int[]
#  - 합한 수 : 100*10^5=10^7 > int(20억까지) 가능
#  - 최대값 : int

import sys
input=sys.stdin.readline

N,K=map(int,input().split())
nums=list(map(int,input().split()))
each=0

# K개 더해주기
for i in range(K):
    each +=nums[i]
maxv=each

# 다음 인덱스 더해주고, 이전 인덱스 빼주기
for i in range(K,N):
    each+=nums[i]
    each-=nums[i-K]
    maxv=max(maxv,each)

print(maxv)
