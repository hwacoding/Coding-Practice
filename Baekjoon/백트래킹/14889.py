# 1. 아이디어 
#  - 한 쪽 팀원만 뽑으면, 반대 팀원도 정해짐
#  - 순열

# 2. 시간복잡도
#  - 4 : 3 | 6 : 10 | 8 : 35 | 10 : 81 | 12 : 162 ...
#  - (n-1)+...+1 => 합

# 3. 자료구조
#  - chk : int[]
#  - mp : int[][]
#  - m : int

import sys
input=sys.stdin.readline
MAX=sys.maxsize

N=int(input())
mp=[list(map(int,input().split())) for _ in range(N)]
chk=[False]*N
chk[0]=True
tmp=[0] # 팀 한 쪽에 무조건 0번은 있기 마련이기에 미리 넣어준다.
res=MAX

def recur(k,lev): # 중복 x하기 위해서 앞에 들어온 k를 알아야 한다.
    global res
    if lev==0:
        a=0
        b=0
        for i in range(N):
            if chk[i]==True:
                for j in range(i,N):
                    if chk[j]==True:
                        a+=mp[i][j]
                        a+=mp[j][i]
            elif chk[i]==False:
                for j in range(i,N):
                    if chk[j]==False:
                        b+=mp[i][j]
                        b+=mp[j][i]

        # print(tmp)
        # print(a,b)
        m=abs(a-b)
        if res>m:
            res=m
        # print(tmp)
        return
    
    for i in range(k,N): # k부터 반복문 진행
        if chk[i]==False:
            chk[i]=True
            tmp.append(i)
            recur(i,lev-1)
            tmp.pop()
            chk[i]=False
        

recur(1,N//2-1)
print(res)