N,T=map(int,input().split())

L=[]
# 0='^' 1='>' 2='v' 3='<'
Rule=['012','013','023','123','01','03','23','12','12','01','03','23']

for i in range(N**2):
    tmp=list(map(int,input().split()))
    L.append(tmp)


visited=[]

def Drive(t,cur_i):
    global T
    global N
    global Rule
    # print('cur_i : ',cur_i,'t : ',t)
    
    if cur_i not in visited:
        visited.append(cur_i)
    if len(visited)==N**2:
        return
   
    if t>=T: 
        return
    else:
        if cur_i>=N and '0' in Rule[L[cur_i][t%4]-1]:
            # print('0 ',t)
            nex_i=cur_i
            nex_i-=N
            Drive(t+1,nex_i)

        if cur_i%N!=N-1 and '1' in Rule[L[cur_i][t%4]-1]:
            # print('1 ',t)
            nex_i=cur_i
            nex_i+=1
            Drive(t+1,nex_i)

        if cur_i<N**2-N and '2' in Rule[L[cur_i][t%4]-1]:
            # print('2 ',t)
            nex_i=cur_i
            nex_i+=N
            Drive(t+1,nex_i)

        if cur_i%N!=0 and '3' in Rule[L[cur_i][t%4]-1]:
            # print('3 ',t)
            nex_i=cur_i
            nex_i-=1
            Drive(t+1,nex_i)


Drive(0,0)

print(len(visited))