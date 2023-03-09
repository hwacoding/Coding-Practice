n=list(map(int,input().split()))

asc=[1,2,3,4,5,6,7,8]
des=[8,7,6,5,4,3,2,1]

flag=0
if flag==0:
    for i in range(8):
        if n[i]!=asc[i]:
            flag=1

if flag==1:
    for i in range(8):
        if n[i]!=des[i]:
            flag=2

if flag==0:
    print("ascending")
elif flag==1:
    print("descending")
elif flag==2:
    print("mixed")