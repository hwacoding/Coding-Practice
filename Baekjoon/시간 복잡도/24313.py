# O(g(n)) = {f(n) | 모든 n ≥ n0에 대하여 f(n) ≤ c × g(n)인 양의 상수 c와 n0가 존재한다}

a=list(map(int,input().split()))
c=int(input())
n=int(input())

f=a[0]*n+a[1]
g=c*n

if a[0]>c:
    print('0')
else:
    if f<=g:
        print('1')
    else:
        print('0')