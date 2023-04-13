# 1. 아이디어
#  - 백트래킹 재귀함수 안에서, for 돌면서 숫자 선택(이때 방문여부 확인)
#  - 재귀함수에서 M개를 선택할 경우 print

# 2. 시간복잡도
#  - N! > 가능

# 3. 자료구조
#  - 결과값 저장 int[]
#  - 방문여부 체크 bool[]

import sys
input=sys.stdin.readline

N,M=map(int,input().split())
rs=[]
chk=[False]*(N+1) # 0번째 사용 안하고, 1~N번째를 사용

def recur(num):
    if num==M:
        print(' '.join(map(str,rs))) # 리스트 값을 ' ' 구분자를 넣어 문자열로 합쳐준다.
        return 

    for i in range(1,N+1):
        if chk[i]==False:
            chk[i]=True
            rs.append(i)
            recur(num+1)
            # 이렇게 하면, [1,2] 출력 이후 [1,2,3]이 된다.
            # 마지막에 넣었던 것을 빼줘야 한다!
            chk[i]=False
            rs.pop()

recur(0)