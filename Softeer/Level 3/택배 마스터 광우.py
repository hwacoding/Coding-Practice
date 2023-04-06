import itertools

N,M,K=map(int,input().split())
L=list(map(int,input().split()))
L=list(itertools.permutations(L,N)) # 가능한 모든 순서 생성

bascket=0
result=0
R=[]

index=0
for i in range(len(L)):
    for j in range(K):
        while 1:
            if bascket+L[i][index%N]>M:
                break
            else:
                bascket+=L[i][index%N]
                index+=1
        result+=bascket
        bascket=0

    R.append(result)
    result=0
    index=0

print(min(R))