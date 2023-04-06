N,M=map(int,input().split())
W=list(map(int,input().split()))

Best=[0 for i in range(N)]
Friendship=[0 for i in range(N)] # 친분 있는지 여부

for i in range(M):
    a,b=map(int,input().split())

    if W[a-1] < W[b-1]:
        if Friendship[b-1]==1 and Best[b-1]==0: # 다른 관계에서 자신이 약하다고 이미 안 경우
            Best[a-1]=0
            Best[b-1]=0
        else:
            Best[a-1]=0
            Best[b-1]=1
    elif W[a-1] > W[b-1]:
        if Friendship[a-1]==1 and Best[a-1]==0:
            Best[a-1]=0
            Best[b-1]=0
        else:
            Best[a-1]=1
            Best[b-1]=0
    else: # 같은 무게를 들 경우
        Best[a-1]=0
        Best[b-1]=0

    Friendship[a-1]=1
    Friendship[b-1]=1

print(Best.count(1) + Friendship.count(0))