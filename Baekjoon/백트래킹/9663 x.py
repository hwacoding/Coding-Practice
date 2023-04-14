# 1. 아이디어
#  - 백트래킹 recur(y) 처음 둔 곳
#  - Queen 둔 곳 저장. 다음 줄에 놓일 수 있는 곳 확인.
#  - Queen 둔 곳 아래, 대각선 확인.(x축) idx 활용.
#  - 줄마다 놓일 수 있는 체스는 한 개다.
#  - N개 다 놓으면 cnt+=1

# 2. 시간복잡도
#  - O(N^(N+1)) -> 불가능
#  - O(N^N)을 만들기 위해서는
#  - 아래, 오른쪽 대각선, 왼쪽 대각선 확인 O(N)을 O(1)로 변경!
#  - 오른쪽 대각선 y-x 값 모두 같음. 왼쪽 대각선 y+x 값 모두 같음.
#  - hashset을 이용하여 O(1)로 만든다.

# 3. 자료구조
#  - Q : int[(y,x)]
#  - cnt : int

# 문제 : chk 복구

import sys
import copy
input=sys.stdin.readline

N=int(input())
# Q=[(0,0) for _ in range(N)]
x_hashset=[0 for _ in range(N)] # x축 hashset
dr_hashset=[0 for _ in range(2*N)] # 오른쪽 대각선 hashset
dl_hashset=[0 for _ in range(2*N)] # 왼쪽 대각선 hashset
res=0

def recur(y):
    global res
    # print('y',y)
    # print(x_hashset) 
    # print(dr_hashset)
    # print(dl_hashset) 
    if N==y:
        res+=1
        # print(Q)
        return
    # print(Q)
    for i in range(N): #x
        # sw=True # 놓을 수 있는지 다 체크
        # for j in range(y): # 놓을 수 있는지 확인
        #     dr=Q[j][1]+y-j # 오른쪽 대각선
        #     dl=Q[j][1]-y+j # 왼쪽 대각선
        #     if Q[j][1]==i:
        #         sw=False
        #         break
        #     if 0<=dr<N and dr==i:
        #         sw=False
        #         break
        #     if 0<=dl<N and dl==i:
        #         sw=False
        #         break
        if x_hashset[i]==0 and dr_hashset[y-i+N]==0 and dl_hashset[y+i]==0:
            # Q[y]=(y,i)
            x_hashset[i]=1  
            dr_hashset[y-i+N]=1
            dl_hashset[y+i]=1
            recur(y+1)
            x_hashset[i]=0
            dr_hashset[y-i+N]=0
            dl_hashset[y+i]=0
            # Q.pop() # 복구


# 0번째 줄에 먼저 하나 둔다.
for i in range(N): # x
    # 저장
    # Q[0]=(0,i)
    x_hashset[i]=1
    dr_hashset[0-i+N]=1
    dl_hashset[0+i]=1
    recur(1)   
 
    x_hashset[i]=0  
    dr_hashset[0-i+N]=0
    dl_hashset[0+i]=0
    # Q.pop()

print(res)