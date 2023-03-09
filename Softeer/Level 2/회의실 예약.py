n,m=map(int,input().split())

name=list()
time=[[0 for i in range(9)] for j in range(n)]

for i in range(n):
    str=input()
    name.append(str)

name.sort() ## 오름차순

for i in range(m):
    str,a,b=input().split()
    name_index=name.index(str) ## list.index('찾고자 하는 문자열')

    for j in range((int(a)-9),(int(b)-9)): ## 예약된 시간 체크
        time[name_index][j]=1
        

for i in range(n):
    p=list() ## available time list
    flag=0

    print("Room",name[i]+":") ## print("a","b") -> a b
                              ## print("a"+"b") -> ab
    
    if time[i].count(0)==0:
        print("Not available")
    else:
        for j in range(9):
            if time[i][j]==0 and flag==0:
                flag=1
                p.append(j+9)
            elif time[i][j]==1 and flag==1:
                flag=0
                p.append(j+9)

        if len(p)%2==1: ## 홀수이면, 마지막 타임까지 예약 가능한 경우임.
            p.append(18)

        print(int(len(p)/2),"available:")
        for j in range(0,len(p),2):
            if p[j]==9:
                print("09-",end="") ## default = print("str", end="\n", sep=" ")
                print(p[j+1])
            else:
                print(p[j],"-",p[j+1],sep="")
            
    if i!=n-1: ## 마지막 줄에는 print 안 하도록
        print("-----")
        