m,n,k=map(int,input().split())

str="" # secret
str_c="" # 입력

s=input().split()

for i in range(m): # string으로 변환
    str+=s[i] 

k=input().split()

for i in range(n):
    str_c+=k[i]

if str in str_c:
    print("secret")
else:
    print("normal")