# 1. 아이디어
#  - 첫 번째
#  - M개의 수마다 각각 어디에 있는지 찾기
#  - for : M개의 수
#  - for : N개의 수 안에 있는지 확인

#  - 두 번째
#  - M개를 확인해야 하는데, 연속하다는 특징 활용 가능? => 불가능
#  - 정렬해서 이진 탐색 가능? => N개의 수 먼저 정렬 => M개의 수 하나씩 이진탐색으로 확인

# 2. 시간복잡도
#  - 첫 번째
#  - for : M개의 수 > O(M)
#  - for : N개의 수 안에 있는지 확인 > O(N)
#  - O(M*N)=10^10 >> 불가능

#  - 두 번째
#  - N개의 수 정렬 : O(N*logN)
#  - M개의 수 이진탐색 : O(M*logN)
#  - O((N+M)logN) = 2*10^5*20 = 4*10^6 >> 가능

# 3. 자료구조
#  - N개 숫자 : int[]
#  - M개 숫자 : int[]

import sys
input=sys.stdin.readline

N=int(input())
nums=list(map(int,input().split))
M=int(input())
target_list=list(map(int,input().split))

nums.sort() # 이진탐색 가능하도록 정렬

def search(st,en,target):
    if st==en:
        if nums[st]==target:
            print(1)
        else:
            print(0)
        return
    
    mid=(st+en)//2
    if nums[mid]<target:
        search(mid+1,en,target)
    else:
        search(st,mid,target)

for each_target in target_list:
    search(0,N-1,each_target)
