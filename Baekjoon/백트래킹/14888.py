# 1. 아이디어
#  - 백트래킹 recur(idx), 계산할 숫자 : idx
#  - idx가 배열 길이랑 같으면, 배열 저장 return
#  - 연산자 배열 4개 for문
#  - 1보다 크면, 하나 빼고 연산 후, 개수-1
#  - 재귀
#  - 재귀 후에 전 값들로 복구

# 2. 시간복잡도
#  - O((N-1)!) : N-1<=10 >> 가능!

# 3. 자료구조
#  - 계산 : int[]
#  - 연산자 : int[4]
#  - res : int[]

import sys
input=sys.stdin.readline

N=int(input())
A=list(map(int,input().split()))
Oper=list(map(int,input().split()))

tmp=A[0]
res=[]

def recur(idx):
    global tmp

    if idx==len(A)-1:
        res.append(tmp)
        return

    b=A[idx+1]

    for i in range(4):
        if Oper[i]>=1:
            Oper[i]-=1
            btmp=tmp
            if i==0:
                # print('+')
                tmp+=b
            elif i==1:
                # print('-')
                tmp-=b
            elif i==2:
                # print('x')
                tmp*=b
            elif i==3:
                # print('/')
                if tmp<0:
                    tmp=-tmp
                    tmp//=b
                    tmp=-tmp
                else:
                    tmp//=b
            recur(idx+1)
            Oper[i]+=1
            tmp=btmp

recur(0)
print(max(res))
print(min(res))