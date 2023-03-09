k,p,n=map(int,input().split())

for i in range(n):
    k=k*p

    if k>=1000000007:
        k=k%1000000007

print(k)