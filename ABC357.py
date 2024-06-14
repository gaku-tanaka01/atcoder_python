N, M = map(int, input().split())

hands_num = list(map(int, input().split()))
count = 0
for i in range(N):
    if (M-hands_num[i] >= 0):
        count += 1
        M -= hands_num[i]
    else:
        break

print(count)
