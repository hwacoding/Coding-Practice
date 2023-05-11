# 1. 아이디어
#  - 이진탐색
#  - 0~max 중간값으로 잘랐을 때, 
#  - 만들 수 있는 랜선 개수가 작으면, 다시 0~중간값
#  - 크면, 중간값~max

# 2. 시간복잡도
#  - O(log(2^31-1))

import sys
input=sys.stdin.readline

K,N=map(int,input().split())
L=[int(input()) for _ in range(K)]

def half(st,ed):
    # print(st,ed)
    if st>ed: # st==ed인 경우가 없기 때문에 st>ed(res>=N인 경우를 걸쳐야만 나온다.)에서 return한다.
        print(st-1) # res>=N인 경우를 걸쳐야만 나오기 때문에 결과값 -1로 수정
        return

    mid=(st+ed)//2

    res=0
    for lan in L:
        res+=lan//mid
    
    if res>=N:
        half(mid+1,ed) # 같을 경우 커져야 하지만, mid도 포함해야 한다고 생각했다. => half(mid,ed)
                       # 그렇게 되면, 200 201에서 무한루프로 반복하게 된다.
                       # 두 가지 case 모두 변화한 값으로 호출하여 해결한다.
    else:
        half(st,mid-1)

half(1,max(L))