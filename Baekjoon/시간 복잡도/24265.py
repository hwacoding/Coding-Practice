# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n - 1
#         for j <- i + 1 to n
#             sum <- sum + A[i] × A[j]; # 코드1
#     return sum;
# }

# O(n^2)

n=int(input())
s=0

for i in range(n):
    s+=i

print(s)
print('2')