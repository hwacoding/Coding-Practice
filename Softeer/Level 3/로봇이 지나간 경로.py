H, W=map(int,input().split())
S=[]
tmp=''

for i in range(H):
    tmp=input()
    S.append(tmp)

cnt=0 # '#'의 개수 카운트
SH=0 # Start H
SW=0 # Start W
flag=0

EH=[]
EW=[]

# 1. #의 끝 찾기
for i in range(H):
    for j in range(W):
        if S[i][j]=='#':
            if i==0:
                if j==0:
                    if S[i+1][j]=='#':
                        cnt+=1
                    if S[i][j+1]=='#':
                        cnt+=1
                elif j==W-1:
                    if S[i+1][j]=='#':
                        cnt+=1
                    if S[i][j-1]=='#':
                        cnt+=1
                else:
                    if S[i+1][j]=='#':
                        cnt+=1
                    if S[i][j+1]=='#':
                        cnt+=1
                    if S[i][j-1]=='#':
                        cnt+=1
            elif i==H-1:
                if j==0:
                    if S[i-1][j]=='#':
                        cnt+=1
                    if S[i][j+1]=='#':
                        cnt+=1
                elif j==W-1:
                    if S[i-1][j]=='#':
                        cnt+=1
                    if S[i][j-1]=='#':
                        cnt+=1
                else:
                    if S[i-1][j]=='#':
                        cnt+=1
                    if S[i][j+1]=='#':
                        cnt+=1
                    if S[i][j-1]=='#':
                        cnt+=1
            else:
                if j==0:
                    if S[i+1][j]=='#':
                        cnt+=1
                    if S[i-1][j]=='#':
                        cnt+=1
                    if S[i][j+1]=='#':
                        cnt+=1
                elif j==W-1:
                    if S[i+1][j]=='#':
                        cnt+=1
                    if S[i-1][j]=='#':
                        cnt+=1
                    if S[i][j-1]=='#':
                        cnt+=1
                else:
                    if S[i+1][j]=='#':
                        cnt+=1
                    if S[i-1][j]=='#':
                        cnt+=1
                    if S[i][j-1]=='#':
                        cnt+=1
                    if S[i][j+1]=='#':
                        cnt+=1
            if cnt==1:
                SH=i
                SW=j
                EH.append(SH)
                EW.append(SW)
                flag+=1
            cnt=0

    if flag==2:
        break

# print(EH,EW)

# 2. 첫 방향 찾기
Ad=[]
dir=''

for i in range(2):
    SH=EH[i]
    SW=EW[i]
    if SH==0:
        if SW==0:
            if S[SH+1][SW]=='#':
                dir='v'
            elif S[SH][SW+1]=='#':
                dir='>'
        elif SW==W-1:
            if S[SH+1][SW]=='#':
                dir='v'
            elif S[SH][SW-1]=='#':
                dir='<'
        else:
            if S[SH+1][SW]=='#':
                dir='v'
            elif S[SH][SW+1]=='#':
                dir='>'
            elif S[SH][SW-1]=='#':
                dir='<'
    elif SH==H-1:
        if SW==0:
            if S[SH-1][SW]=='#':
                dir='^'
            elif S[SH][SW+1]=='#':
                dir='>'
        elif SW==W-1:
            if S[SH-1][SW]=='#':
                dir='^'
            elif S[SH][SW-1]=='#':
                dir='<'
        else:
            if S[SH-1][SW]=='#':
                dir='^'
            elif S[SH][SW+1]=='#':
                dir='>'
            elif S[SH][SW-1]=='#':
                dir='<'
    else:
        if SW==0:
            if S[SH+1][SW]=='#':
                dir='v'
            elif S[SH-1][SW]=='#':
                dir='^'
            elif S[SH][SW+1]=='#':
                dir='>'
        elif SW==W-1:
            if S[SH+1][SW]=='#':
                dir='v'
            elif S[SH-1][SW]=='#':
                dir='^'
            elif S[SH][SW-1]=='#':
                dir='<'
        else:
            if S[SH+1][SW]=='#':
                dir='v'
            elif S[SH-1][SW]=='#':
                dir='^'
            elif S[SH][SW-1]=='#':
                dir='<'
            elif S[SH][SW+1]=='#':
                dir='>'
    Ad.append(dir)

# print(Ad)

# 3. 명령

Ac=[]

for k in range(2):   
    SH=EH[k]
    SW=EW[k]
    dir=Ad[k]

    C=[[0 for i in range(W)] for j in range(H)] # 방문 체크
    C[SH][SW]=1

    if dir=='>': # 처음 이동
        C[SH][SW+1]=1
        C[SH][SW+2]=1
        SW+=2 
    elif dir=='<':
        C[SH][SW-1]=1
        C[SH][SW-2]=1
        SW-=2
    elif dir=='v':
        C[SH+1][SW]=1
        C[SH+2][SW]=1
        SH+=2
    elif dir=='^':
        C[SH-1][SW]=1
        C[SH-2][SW]=1
        SH-=2

    com='A'
     

    while 1:
        if dir=='>':
            if SH==0:
                if C[SH+1][SW]==0 and S[SH+1][SW]=='#':
                    com+='R'
                    dir='v'
                elif SW!=W-1 and S[SH][SW+1]=='#':
                    com+='A'
                    C[SH][SW+1]=1
                    C[SH][SW+2]=1
                    SW+=2
                else:
                    break
            elif SH==H-1:
                if C[SH-1][SW]==0 and S[SH-1][SW]=='#':
                    com+='L'
                    dir='^'
                elif SW!=W-1 and S[SH][SW+1]=='#':
                    com+='A'
                    C[SH][SW+1]=1
                    C[SH][SW+2]=1
                    SW+=2
                else:
                    break
            else:
                if C[SH+1][SW]==0 and S[SH+1][SW]=='#':
                    com+='R'
                    dir='v'
                elif C[SH-1][SW]==0 and S[SH-1][SW]=='#': # 위에서 내려온 경우
                    com+='L'
                    dir='^'
                elif SW!=W-1 and S[SH][SW+1]=='#':
                    com+='A'
                    C[SH][SW+1]=1
                    C[SH][SW+2]=1
                    SW+=2
                else:
                    break
        elif dir=='<':
            if SH==0:
                if C[SH+1][SW]==0 and S[SH+1][SW]=='#':
                    com+='L'
                    dir='v'
                elif SW!=0 and S[SH][SW-1]=='#':
                    com+='A'
                    C[SH][SW-1]=1
                    C[SH][SW-2]=1
                    SW-=2
                else:
                    break
            elif SH==H-1:
                if C[SH-1][SW]==0 and S[SH-1][SW]=='#':
                    com+='R'
                    dir='^'
                elif SW!=0 and S[SH][SW-1]=='#':
                    com+='A'
                    C[SH][SW-1]=1
                    C[SH][SW-2]=1
                    SW-=2
                else:
                    break
            else:
                if C[SH+1][SW]==0 and S[SH+1][SW]=='#':
                    com+='L'
                    dir='v'
                elif C[SH-1][SW]==0 and S[SH-1][SW]=='#':
                    com+='R'
                    dir='^'
                elif SW!=0 and S[SH][SW-1]=='#':
                    com+='A'
                    C[SH][SW-1]=1
                    C[SH][SW-2]=1
                    SW-=2
                else:
                    break

        elif dir=='^':
            if SH==0:
                if SW!=W-1 and C[SH][SW+1]==0 and S[SH][SW+1]=='#':
                    com+='R'
                    dir='>'
                elif SW!=0 and C[SH][SW-1]==0 and S[SH][SW-1]=='#':
                    com+='L'
                    dir='<'
                else:
                    break
            else:
                if S[SH-1][SW]=='#':
                    com+='A'
                    C[SH-1][SW]=1
                    C[SH-2][SW]=1
                    SH-=2
                elif SW!=0 and C[SH][SW-1]==0 and S[SH][SW-1]=='#':
                    com+='L'
                    dir='<'
                elif SW!=W-1 and C[SH][SW+1]==0 and S[SH][SW+1]=='#':
                    com+='R'
                    dir='>'
                else:
                    break
        elif dir=='v':
            if SH==H-1:
                if SW!=W-1 and C[SH][SW+1]==0 and S[SH][SW+1]=='#':
                    com+='L'
                    dir='>'
                elif SW!=0 and C[SH][SW-1]==0 and S[SH][SW-1]=='#':
                    com+='R'
                    dir='<'
                else:
                    break
            else:
                if S[SH+1][SW]=='#':
                    com+='A'
                    C[SH+1][SW]=1
                    C[SH+2][SW]=1
                    SH+=2
                elif SW!=0 and C[SH][SW-1]==0 and S[SH][SW-1]=='#':
                    com+='R'
                    dir='<'
                elif SW!=W-1 and C[SH][SW+1]==0 and S[SH][SW+1]=='#':
                    com+='L'
                    dir='>'
                else:
                    break

    Ac.append(com)

    # print(com)
    # print(dir)

idx=0

if len(Ac[0])>len(Ac[1]):
    idx=1


print(EH[idx]+1,EW[idx]+1)
print(Ad[idx])
print(Ac[idx])