N,M,K=map(int,input().split())

a=list(map(int,input().split()))
b=list(map(int,input().split()))

# a 기준으로 순서대로 b 하나씩 비교.
# 같으면, 앞에꺼 비교 = O(N^2*M)
# 이미 앞에꺼 비교했기 때문에, 그 값을 c[i][j]에 저장 = O(N*M)
# if a[i]==b[j] -> a[i-1], b[j-1] 같은지 확인

c=[[0 for i in range(M)] for j in range(N)]

for i in range(N):
    for j in range(M):
        if a[i]==b[j]:
            if i!=0 and j!=0 and c[i-1][j-1]!=0:
                c[i][j]=c[i-1][j-1]+1
            else:
                c[i][j]=1

m=0
for i in range(N):
    if m<max(c[i]):
        m=max(c[i])

print(m)