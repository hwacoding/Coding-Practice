n,m=map(int,input().split())

l=[[0 for i in range(2)] for j in range(n)] ##빌딩 구간
k=[[0 for i in range(2)] for j in range(m)] ##검사

for i in range(n):
    a,b=map(int,input().split())
    l[i][0]=a
    l[i][1]=b

for i in range(m):
    a,b=map(int,input().split())
    k[i][0]=a
    k[i][1]=b

max=0
l_index=0
k_index=0
floor_1=l[l_index][0]
floor_2=k[k_index][0]

while 1: ## while 조건문으로 floor_1!=100 or floor_2!=100으로 넣으면, n, m이 1일 때 값이 들어오지 않는다.
    if l[l_index][1]<k[k_index][1]:
        if max<k[k_index][1]-l[l_index][1]:
            max=k[k_index][1]-l[l_index][1]

    if floor_1==100 and floor_2==100: ##그래서 max값 비교 후, 조건을 통해 break
        break

    if floor_1>floor_2:
        k_index+=1
        floor_2+=k[k_index][0]
    elif floor_1<floor_2:
        l_index+=1
        floor_1+=l[l_index][0]
    else: ##같을 때
        l_index+=1
        k_index+=1
        floor_1+=l[l_index][0]
        floor_2+=k[k_index][0]

print(max)