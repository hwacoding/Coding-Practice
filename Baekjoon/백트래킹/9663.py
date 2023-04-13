# 1. 아이디어
#  - 백트래킹 recur(y) 처음 둔 곳
#  - 놓일 수 있는지 확인
#  - 놓이면, 그 다음 줄부터 보면 된다. Queen은 가로줄 다 먹기 때문
#  - 줄마다 놓일 수 있는 체스는 한 개다.
#  - N개 다 놓으면 cnt+=1

# 2. 시간복잡도
#  - O(N!) -> 시간 제한 10초이므로 가능

# 3. 자료구조
#  - chk : int[][]
#  - cnt : int

import sys
input=sys.stdin.readline

N=int(input())
chk=[[False]*N for _ in range(N)]
tmp_chk=[[False]*N for _ in range(N)]
cnt=1
res=0

def recur(y):
    global cnt
    global res
    global chk
 
    if y==N:
        return
    
    if cnt==N:
        res+=1
        return

    # 처음 둔 곳 다음 줄부터 체크
    for i in range(N): # x            
        for k in chk:
            print(k)
        print('y,x',y,i)
        if chk[y][i]==False:        

            for j in range(N):
                chk[j][y]=True # 세로
                chk[y][j]=True # 가로

            idx=1
            while 1: # 대각선 아래 두 방향
                if y+idx<N and i+idx<N:
                    chk[y+idx][i+idx]=True
                    idx+=1
                else:
                    break

            idx=1
            while 1:
                if 0<=y-idx and 0<=i-idx:
                    chk[y-idx][i-idx]=True
                    idx+=1
                else:
                    break
            
            cnt+=1
            tmp_chk=chk.copy()
            recur(y+1) 

            # 내려갔다가 올라와서 다시 봐야함.
            # chk 복구
            chk=tmp_chk.copy()
            
            cnt-=1

# 0번째 줄에 먼저 하나 둔다.
for i in range(N): # x
    # 하나 두면, chk 가로, 세로, 대각선 방향 모두 True로 변경
    for j in range(N):
        chk[j][0]=True # 세로
        chk[0][j]=True # 가로

    idx=1
    while 1: # 대각선은 아래 두 방향만 진행하면 된다.
        if i+idx<N:
            chk[idx][i+idx]=True
            idx+=1
        else:
            break
    
    idx=1
    while 1:
        if 0<=i-idx:
            chk[idx][i-idx]=True
            idx+=1
        else:
            break
    print("외부 콜")
    recur(1)        
        # for b in chk:
        #     print(b)
    chk=[[False]*N for _ in range(N)]
    cnt=1

print(res)