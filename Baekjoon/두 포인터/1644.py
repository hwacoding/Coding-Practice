# 1. 아이디어
#  - 소수 배열 생성
#  - for sqrt(N) : 2번
#  - 두 포인터
#  - 앞 포인터 값이 크면, break

# 2. 시간복잡도
#  - 소수 배열 생성 : O(Nlog(log(N)))
#  - 두 포인터 : O(N)
#  - O(N) : N=4백만 >> 가능!

# 3. 자료구조
#  - nums : int[]
#  - prime : int[]
#  - fp, ep : int

import sys
input=sys.stdin.readline

N=int(input())
nums=[True]*(N+1)
# nums[0]=False
# nums[1]=False
prime=[]

# 에라토스테네스의 체
for i in range(2,int(N**0.5)+1):
    if nums[i]==True: # 소수일 경우
        for j in range(2,N//i+1):
            nums[i*j]=False

for i in range(2,N+1):
    if nums[i]==True:
        prime.append(i)

# print(prime)

sum=0
fp=0
ep=0
res=0
while 1:
    if sum>=N:
        if sum==N:
            res+=1
        sum-=prime[fp]
        fp+=1
    else: # 작을 경우
        if ep==len(prime):
            break # 작은데 더 커질 수 없으면, 끝
        sum+=prime[ep]
        ep+=1 

        
    # print(sum)
print(res)