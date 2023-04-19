# 1. 아이디어 
#  - 첫 번째
#  - for문 : N개, tree가 설정 높이보다 크면, sum=trees[N]-M
#  - for문 : M개, sum이 M보다 크거나 같으면 break

#  - 두 번째
#  - M이 최대 20억이기 때문에 M으로 돌리면 안된다.
#  - 1) 구하고자 하는 것 = height (1<=height<=1,000,000)
#  - 2) height<tree : sum+=tree-height
#  -    sum>=M : 끝


# 2. 시간복잡도
#  - 첫 번째
#  - O(N*M) >> 불가능

#  - 두 번째
#  - 1) O(N)
#  - 2) O(N)
#  - O(N*N) >> 불가능!
#  - 1번을 이진 기법 활용! : O(log(N))
#  - O(Nlog(N)) : 1,000,000 * 30 >> 3천만 < 2억 =>> 가능!

# 3. 자료구조
#  - trees : int[]
#  - sum : int


import sys
input=sys.stdin.readline

N,M=map(int,input().split())
trees=list(map(int,input().split()))

h=0
st=1
en=max(trees)

while 1:
    if st==en:
        h=en
        break

    sum=0
    mid=(st+en)//2

    for tree in trees:
        if tree>mid:
            sum+=tree-mid 

    if sum>=M:
        st=mid+1
    else:
        en=mid

    # print(st,en)
print(h-1)