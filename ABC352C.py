N = int(input())
A = []
B = []

for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

dif = -1
index = -1

for i in range(N):
    if (abs(A[i] - B[i]) > dif or dif == -1):
        dif = abs(A[i] - B[i])
        index = i

sum = 0
for i in range(N):
    if (i != index):
        sum += A[i]
    else:
        sum += B[i]

print(sum)


