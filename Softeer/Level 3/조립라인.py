N=int(input())
T=[]

for i in range(N):
    a=list(map(int,input().split()))
    T.append(a)

# Idea
# 조립라인 A, B의 i번째 작업장으로 올 수 있는 방법은 2가지.
# A, B의 i번째 작업장을 기준으로 하여 2가지 중 최소를 구한다.
# 마지막에 A, B의 N번째 작업장에서 최솟값이 답.

# 초기값
a=T[0][0]
b=T[0][1]

for i in range(N-1):
    A1=b+T[i][3]+T[i+1][0] # B에서 오는 경우
    A2=a+T[i+1][0] # A에서 오는 경우

    B1=a+T[i][2]+T[i+1][1] # A에서 오는 경우
    B2=b+T[i+1][1] # B에서 오는 경우

    if A1>A2:
        a=A2
    else:
        a=A1
    # print(A1,A2)

    if B1>B2:
        b=B2
    else:
        b=B1
    # print(B1,B2)
    
print(min(a,b))