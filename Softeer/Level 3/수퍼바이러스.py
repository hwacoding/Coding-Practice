K,P,N=map(int,input().split())

#홀수이면, pow(K,int(N/2))*K
#N을 소인수분해 2로. 2*2*2*2*...+1

def fun(p,n):
    if n==1:
        return p
    elif n%2==0:
        a=fun(p,n/2)
        return a*a
    else:
        a=fun(p,n//2)
        return a*a*p

print(K*fun(P,10*N))