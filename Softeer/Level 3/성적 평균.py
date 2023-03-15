N,K = map(int,input().split())

Score = list(map(int,input().split()))
sum=0

for i in range(K):
    a,b=map(int,input().split())
    
    for j in range(a,b+1):
        sum+=Score[j-1]
    
    print(format(sum/(b-a+1),".2f")) ## format(int, ".2f") 소수점 두 번째 자리까지 표시
                                     ## = 소수점 세 번째 자리에서 반올림
    sum=0