# 1. 아이디어
#  - 공유기 좌표 정렬
#  - 구하고자 하는 값 = 공유기 사이 최대 거리
#  - 최소 거리와 최대 거리 사이에서 나오는 결과
#  - 중간 거리로 했을 때, 넣을 수 있는 공유기 개수 확인

#  -- ★ 구하고자 하는 값 범위 내에서 이분 탐색하는 경우가 많으니 기준을 잘 잡자! ★--

# 2. 시간복잡도
#  - O(Nlog(N)) : 이진 탐색으로 고른 값을 N개에서 가능한 공유기 선택
 
import sys
input=sys.stdin.readline

N,C=map(int,input().split())
x=[int(input()) for _ in range(N)]
x.sort()

def half(st,ed):
    # print("st,ed",st,ed)
    mid=(st+ed)//2
    
    if st>ed: # 역전 당하면,
        print(st-1) # half(mid+1,ed)에서 온 것이기 때문에 결과값은 st-1이다.
        return

    cnt=1
    k=x[0]
    for i in range(1,N):
        # print("k,x[i]",k,x[i])
        if abs(k-x[i])>=mid:
            cnt+=1
            k=x[i]
    # print("mid, cnt",mid,cnt)

    if cnt>=C: # 개수 같으면, 최대 길이를 구해야 하기 때문에 길이 늘려본다.
        half(mid+1,ed)
    else:
        half(st,mid-1)
        

s=1
e=x[len(x)-1]-x[0]

half(s,e)
