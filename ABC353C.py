N = int(input())
A = list(map(int, input().split()))
sum = 0
for i in range(0, N - 1):
    for j in range(i+1, N):
        sum += (A[i] + A[j]) % (10 ** 8)

print(sum)
