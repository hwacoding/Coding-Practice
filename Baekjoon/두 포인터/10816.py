# 1. 아이디어
#  - Narr sort해서 각 숫자 개수 배열 생성
#  - 이진 탐색 : sort

# 2. 시간복잡도
#  - O(Nlog(N)) : sort
#  - O(N) : 개수 파악
#  - O(Mlog(N)) : M=500,000, N=500,000
#  - 500,000*20 >> 가능

# 3. 자료구조
#  - N,M : int
#  - Narr, Marr : int[]

import sys
input=sys.stdin.readline

N=int(input())
Narr=list(map(int,input().split()))

M=int(input())
Marr=list(map(int,input().split()))

Narr.sort()
cnt=[]
tmp=1
for i in range(N):
    if i+1!=N and Narr[i]==Narr[i+1]:
        tmp+=1
    else:
        cnt.append((Narr[i],tmp))
        tmp=1

# print(cnt)

def find(st,ed,k):
    if st==ed:
        if cnt[st][0]==k:
            print(cnt[st][1], end=" ")
        else:
            print(0, end=" ")
        return
    
    mid=(st+ed)//2
    if cnt[mid][0]<k:
        find(mid+1,ed,k)
    else:
        find(st,mid,k)
    # elif cnt[mid][0]>k:
    #     find(st,mid,k)
    # else: # 같을 경우
    #     print(cnt[mid][1], end=" ")

for i in range(M):
    find(0,len(cnt)-1,Marr[i])



#                     --- dictionary 활용한 코딩 ---
# dic = {}
# for i in Narr:
#     if i in dic:
#         dic[i] += 1
#     else:
#         dic[i] = 1

# for i in Marr:
#     res=dic.get(i)
#     if res==None:
#         print(0,end=" ")
#     else:
#         print(res,end=" ")