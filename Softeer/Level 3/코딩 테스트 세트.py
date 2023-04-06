def test(testSets):
    print(testSets)
    now=c[0] # 
    for i in range(N):
        if now>=testSets:
            now=c[i+1]+d[i]
        elif now+d[i]>=testSets:
            now=c[i+1]+(now+d[i]-testSets)
        else:
            return False
        
    if now>=testSets:
        return True
    else:
        return False

def bSearch(start, end):
    if start==end:
        return start
    
    mid=(start+end+1)//2
    if test(mid):
        return bSearch(mid,end)
    else:
        return bSearch(start,mid-1)

N,T=map(int,input().split())

for i in range(T):
    tmp=list(map(int,input().split()))
    c=[]
    d=[]

    for i in range(len(tmp)):
        if i%2==0:
            c.append(tmp[i])
        else:
            d.append(tmp[i])

    bSearch(0,2*10**12)