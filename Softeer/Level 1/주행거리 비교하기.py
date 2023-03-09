a, b=map(int,input().split()) 
##input().split()으로 읽어오면, str이기 때문에 map을 활용하여 int로 받아온다.

if a>b:
    print("A")
elif a<b:
    print("B")
else:
    print("same")