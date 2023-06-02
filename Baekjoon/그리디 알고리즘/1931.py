# 1. 아이디어
#  - 강의시간 짧은 순으로 넣으면 된다. : 그리디
#  - 끝나는 시간 빠른 순으로 배정
#  - 회의의 시작시간과 끝나는 시간이 같을 수도 있기 때문에 끝나는 시간이 같다면,
#  - 시작 시간 빠른 강의 먼저 배정

# 2. 시간복잡도
#  - O(Nlog(N))

import sys
input=sys.stdin.readline

N=int(input())
A=[list(map(int,input().split())) for _ in range(N)]

A.sort(key=lambda x:(x[1],x[0]-x[1]))
# print(A)

end=A[0][1]
cnt=1
for i in range(1,N):
    if end<=A[i][0]:
        cnt+=1
        end=A[i][1]

print(cnt)
