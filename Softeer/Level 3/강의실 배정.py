# Idea
# 끝나는 시간을 기준으로 정렬

N=int(input())
L=[]

for i in range(N):
    l=list(map(int,input().split()))
    L.append(l)

L.sort(key=lambda x:x[1])

cnt=1
t=L[0][1]
for i in range(1,N):
    if t<=L[i][0]:
        cnt+=1
        t=L[i][1]

print(cnt)