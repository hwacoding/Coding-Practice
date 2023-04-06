N,M=map(int,input().split())

Ice=[]

def check(n,m):
    global Ice
    global N,M

    if Ice[n-1][m]==0: # 위
        if n-1==0 or (not(Ice[n-2][m]==1 and Ice[n-1][m-1]==1 and Ice[n-1][m+1]==1)):
            # 가장자리이거나 사방이 모두 1이 아니라면, 한 개 더 찾으면 된다.
            if Ice[n+1][m]==0: # 아래
                if n+1==N-1: # 가장자리
                    return 0
                elif not(Ice[n+2][m]==1 and Ice[n+1][m-1]==1 and Ice[n+1][m+1]==1):
                    return 0
            if Ice[n][m-1]==0: # 왼쪽
                if m-1==0:
                    return 0
                elif not(Ice[n-1][m-1]==1 and Ice[n+1][m-1]==1 and Ice[n][m-2]==1):
                    return 0
            if Ice[n][m+1]==0: #오른쪽
                if m+1==M-1:
                    return 0
                elif not(Ice[n-1][m+1]==1 and Ice[n+1][m+1]==1 and Ice[n][m+2]==1):
                    return 0
    
    if Ice[n+1][m]==0: # 아래
        if n+1==N-1 or not (Ice[n+2][m]==1 and Ice[n+1][m-1]==1 and Ice[n+1][m+1]==1):
            if Ice[n-1][m]==0:
                if n-1==0:
                    return 0
                elif not(Ice[n-2][m]==1 and Ice[n-1][m-1]==1 and Ice[n-1][m+1]==1):
                    return 0
            if Ice[n][m-1]==0:
                if m-1==0:
                    return 0
                elif not(Ice[n-1][m-1]==1 and Ice[n+1][m-1]==1 and Ice[n][m-2]==1):
                    return 0
            if Ice[n][m+1]==0:
                if m+1==M-1:
                    return 0
                elif not(Ice[n-1][m+1]==1 and Ice[n+1][m+1]==1 and Ice[n][m+2]==1):
                    return 0

    if Ice[n][m+1]==0: # 오른쪽
        if m+1==M-1 or not (Ice[n-1][m+1]==1 and Ice[n+1][m+1]==1 and Ice[n][m+2]==1):
            if Ice[n-1][m]==0:
                if n-1==0:
                    return 0
                elif not(Ice[n-2][m]==1 and Ice[n-1][m-1]==1 and Ice[n-1][m+1]==1):
                    return 0
            if Ice[n][m-1]==0:
                if m-1==0:
                    return 0
                elif not(Ice[n-1][m-1]==1 and Ice[n+1][m-1]==1 and Ice[n][m-2]==1):
                    return 0
            if Ice[n+1][m]==0:
                if n+1==N-1:
                    return 0
                elif not(Ice[n+2][m]==1 and Ice[n+1][m-1]==1 and Ice[n+1][m+1]==1):
                    return 0
                
    if Ice[n][m-1]==0: # 왼쪽
        if m-1==0 or not(Ice[n-1][m-1]==1 and Ice[n+1][m-1]==1 and Ice[n][m-2]==1):
            if Ice[n-1][m]==0:
                if n-1==0:
                    return 0
                elif not(Ice[n-2][m]==1 and Ice[n-1][m-1]==1 and Ice[n-1][m+1]==1):
                    return 0
            if Ice[n][m+1]==0:
                if m+1==M-1:
                    return 0
                elif not(Ice[n-1][m+1]==1 and Ice[n+1][m+1]==1 and Ice[n][m+2]==1):
                    return 0
            if Ice[n+1][m]==0:
                if n+1==N-1:
                    return 0
                elif not(Ice[n+2][m]==1 and Ice[n+1][m-1]==1 and Ice[n+1][m+1]==1):
                    return 0

    return 1     

for i in range(N):
    l=list(map(int,input().split()))
    Ice.append(l)

result=0
flag=0
C=[[0 for i in range(M)] for j in range(N)]
for i in range(N):
    for j in range(M):
        C[i][j]=Ice[i][j]

# print(C)
while 1:
    for i in range(N):
        if Ice[i].count(1)!=0:
            flag=1
            break
        else:
            flag=0

    if flag==0:
        break
    else:
        result+=1
        for i in range(N):
            for j in range(M):
                if Ice[i][j]==1: 
                    C[i][j]=check(i,j) # 녹으면 0
                    
    for i in range(N):
        print(Ice[i])
        for j in range(M):
            Ice[i][j]=C[i][j]

print(result)