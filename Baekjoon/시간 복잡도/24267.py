# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n - 2
#         for j <- i + 1 to n - 1
#             for k <- j + 1 to n
#                 sum <- sum + A[i] × A[j] × A[k]; # 코드1
#     return sum;
# }

# O(n^3)

n=int(input())
s=0
tmp=0

for i in range(n-2,0,-1):
    tmp+=i
s+=tmp

for i in range(n-2):
    tmp-=n-2-i
    s+=tmp

# 수행 횟수는 O(n)으로 처리

print(s)
print('3')