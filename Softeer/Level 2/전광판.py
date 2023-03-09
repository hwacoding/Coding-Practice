t=int(input())

#  0
# 1 2
#  3
# 4 5
#  6

number=[[1,1,1,0,1,1,1],[0,0,1,0,0,1,0],[1,0,1,1,1,0,1],
        [1,0,1,1,0,1,1],[0,1,1,1,0,1,0],[1,1,0,1,0,1,1],
        [1,1,0,1,1,1,1],[1,1,1,0,0,1,0],[1,1,1,1,1,1,1],
        [1,1,1,1,0,1,1]]

def switch_count(big,small):
    count=0
    index_b=len(big)-len(small)
    for i in range(len(small)):
        for j in range(7):
            if number[int(big[index_b][j])]!=number[int(small[i][j])]:
                count+=1
        index_b+=1
        print(index_b)
    
    return count

result=0

for i in range(t):
    a,b=input().split()
    
    for j in range(abs(len(a)-len(b))): ##길이가 다를 경우
        if len(a)>len(b):
            result+=number[int(a[j])].count(1)
        elif len(b)>len(a):
            result+=number[int(b[j])].count(1)

    if len(a)>len(b): ##문자열 길이 수정
        a=a[len(a)-len(b):]
    elif len(b)>len(a):
        b=b[len(b)-len(a):]

    for j in range(len(a)):
        for k in range(7):
            if number[int(a[j])][k]!=number[int(b[j])][k]:
                result+=1

    print(result)
    result=0