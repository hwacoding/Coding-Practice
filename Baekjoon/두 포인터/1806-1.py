# 1. 아이디어
#  - S 이상인 연속된 숫자 합의 길이 저장 -> 두 포인터
#  - left, right = 0
#  - 작으면, right+=1
#  - 크거나 sum 증가할 수 없는 경우, left+=1
#  - 모든 경우를 봐야하기 때문에 left==N이면, break

# 2. 시간복잡도
#  - O(N)


import sys
input=sys.stdin.readline

N,S=map(int,input().split())
nums=list(map(int,input().split()))

sum=0
left=0
right=0
cnt=0
res=100000

while 1:
    if left==N:
        break
    
    if sum<S and right<N:
        sum+=nums[right]
        right+=1
        cnt+=1
    else: # --★ 크거나 sum이 증가하지 못하는 경우 ★--
        if sum>=S and res>cnt: # 최소 길이 갱신
            # print(sum,left,right)
            res=cnt
        sum-=nums[left]
        left+=1
        cnt-=1
        
if res==100000:
    print(0)
else:
    print(res)