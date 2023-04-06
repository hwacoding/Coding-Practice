N,K=map(int,input().split())

L=list(input()) # string -> list
# 물품 기준
# 잡한 물품 G, 물품 잡은 로봇 C, 안 잡히는 물품 X

# H_L=[]
# H_R=[]

# while 1:
#     if L.count('H')==0:
#         break
#     else:
#         k=L.index('H')
#         for i in range(-1,-K-1,-1):
#             if k+i<0:
#                 break
#             else:
#                 if L[k+i]=='P':
#                     H_L.append(abs(i)) # 거리

#         for i in range(1,K+1):
#             if k+i>len(L)-1:
#                 break
#             else:
#                 if L[k+i]=='P':
#                     H_R.append(abs(i))

#         if len(H_L)==0 and len(H_R)==0:
#             L[k]='X'
#         elif len(H_L)==0 and len(H_R)!=0:
#             L[k]='G'
#             L[k+max(H_R)]='C'
#         elif len(H_R)==0 and len(H_L)!=0:
#             L[k]='G'
#             L[k-max(H_L)]='C'
#         else:
#             if max(H_L)>=max(H_R):
#                 L[k]='G'
#                 L[k-max(H_L)]='C'
#             else:
#                 L[k]='G'
#                 L[k+max(H_R)]='C'

#         # print(H_L)
#         # print(H_R)
#         H_L=[]
#         H_R=[]
#         # print(L)

# print(L.count('C'))

flag=0
index=0
while 1:
    if L.count('P')==0:
        break
    else:
        p=L.index('P')
        if p-K<0:
            S=L[:p+K+1]
            index=0
        elif p+K>len(L)-1:
            S=L[p-K:]
            index=p-K
        else:
            S=L[p-K:p+K+1]
            index=p-K
            # print(S)

        # print(S)
        for i in range(len(S)):
            if S.count('H')==0:
                break
            elif S[i]=='H':
                flag=1
                L[index+i]='G'
                L[p]='C'
                break
        
        if flag==0:
            L[p]='X' # 잡을 수 있는 물품 없음

        flag=0
    # print(L)
    
print(L.count('C'))