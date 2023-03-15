N=int(input())
A=list(map(int,input().split()))

B=[1 for i in range(len(A))] ## 각각의 다리까지 오는데, 밟을 수 있는 최대 수

for i in range(len(B)): ## 기준 다리
    for j in range(i,len(B)): ## 비교 다리
        if A[i]<A[j] and B[i]==B[j]: ## 1. 동쪽에 있는 다리가 더 높은지
                                     ## 2. i-1번째 다리까지 밟았을 때, B[i]<B[j]보다 크면 밟지 않는다.
            B[j]+=1

print(max(B))
