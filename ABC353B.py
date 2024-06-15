N, K = map(int, input().split())
groups = list(map(int, input().split()))
count = 0
K_tmp = K
i = 0
while (len(groups) > i):
    if (K_tmp >=groups[i]):
        K_tmp -= groups[i]
        i += 1
    else:
        K_tmp = K
        count += 1

print(count + 1)


