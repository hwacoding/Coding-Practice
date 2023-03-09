w, n=map(int,input().split())

a=[[0 for i in range(2)] for j in range(n)]

for i in range(n):
    b,c=map(int,input().split())
    a[i][0]=b
    a[i][1]=c

a.sort(key=lambda a:-a[1]) ## arr.sort() 원본 수정
                           ## key=lambda a:a[1] 두 번째 인자를 기준으로 오름차순
                           ## key=lambda a:-a[1] 두 번째 인자를 기준으로 내림차순

result=0
cur_w=0 ##current weight
for i in range(n):
    if w>=cur_w+a[i][0]:
        result+=a[i][0]*a[i][1]
        cur_w+=a[i][0]
    else:
        result+=(w-cur_w)*a[i][1]
        break

print(result)