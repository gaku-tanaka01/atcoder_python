N = int(input())
heights = list(map(int, input().split()))

# max = 0
count = 0

for i in range(1, N):
    if (heights[0] < heights[i]):
        # max = heights[i]
        count = i + 1
        break

if (count == 0):
    print(-1)
else:
    print(count)