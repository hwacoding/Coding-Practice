n=int(input())
result=1

def fac(n):
    global result

    if n==0:
        return
    else:
        result=result*n
        fac(n-1)

fac(n)
print(result)