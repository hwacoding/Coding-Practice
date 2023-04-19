# 1. 아이디어
#  - S 이상인 연속된 숫자 합의 길이 저장 -> 최소 출력
 
#  - 연속된 수 -> 두 포인터 활용 가능
#  - 앞에부터 더하고, S 이상이면 => 현재 최소 길이
#  - 앞에 숫자 빼고, 뒤에 숫자 더함 -> 만약, S보다 크면 앞에 하나 더 뺌
#    => 가능하면, 현재 최소 길이 갱신

# 2. 시간복잡도
#  - O(N) :


import sys
input=sys.stdin.readline

N,S=map(int,input().split())
nums=list(map(int,input().split()))

sum=0
left=0
right=0
res=0

sw=False
for i in range(N):
    sum+=nums[i]

    if sum>=S:
        right=i+1
        res=right-left+1
        sw=False
        break
    else:
        sw=True

if sw==False:
    while 1:
        # print(left,right,res)
        if sum>=S: # 클 때,
            if right-left+1<res: # min 확인
                res=right-left+1
            sum-=nums[left]
            left+=1
        else:
            sum+=nums[right]
            right+=1         
            if right==len(nums):
                break
            
else:
    print(0)

print(res)