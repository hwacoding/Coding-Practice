#3 5 9 17 

a=int(input())
n=2

for i in range(a):
    n+=n-1

print(pow(n,2))