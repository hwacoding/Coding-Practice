N,M=map(int,input().split())

L=[]
for i in range(N):
    l=input()
    L.append(l)

A=[[0 for i in range(N)] for j in range(N)]

flag=0
for i in range(N):
    for j in range(i+1,N):
        for k in range(M):
            if L[i][k]=='.' or L[j][k]=='.' or L[i][k]==L[j][k]:
                flag=1
            else:
                flag=0
                break
        if flag==1:
            A[i][j]=1

B=[0 for i in range(N)] # 대체 가능한지 check
result=0

for i in range(N-1,-1,-1):
    if A[i].count(1)==0:
        B[i]=1
        for j in range(N):
            if A[j][i]==1:
                B[j]=1
        result+=1
    # else:
    #     if B[i]==0:
    #         k=B[i].index(1)
    #         for j in range(N):
    #             if A[j][k]==1 and B[j]==0:
    #                 B[j]=1
    #         result+=1

C=[]
for i in range(N):
    if B[i]==0:
        c=[i, A[i]]
        C.append(c)
print(C)
# 1 있는 것들. 1이 적은거 먼저 처리해야지?


print(result)
