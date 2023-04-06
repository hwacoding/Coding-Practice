N=int(input())

A=[[0 for i in range(N)] for j in range(N)]

for i in range(N-1):
    tmp=list(map(int,input().split()))
    A[tmp[0]-1][tmp[1]-1]=tmp[2]
    A[tmp[1]-1][tmp[0]-1]=tmp[2]

B=A[0].copy() # B=A[0]로 하면, 포인터. copy()로 복사한다.
# 1 출발 값 구하기
for i in range(N):
    if B[i]>0:
        for j in range(i+1,N):
            if A[i][j]>0:
                B[j]=B[i]+A[i][j]
print(B)
print(A)

S=[]
S.append(sum(B))

for i in range(1,N):
    for j in range(N):
        if A[i][j]>0:
            S.append(S[j]+A[i][j]*(A[i].count(0)-1))
            break
print(S)