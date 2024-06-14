N = int(input())
nums = {}
for i in range(N):
    tmp = input()
    for j, digit in enumerate(tmp):
        nums[(i, j)] = int(digit)

# for i in range(N):
#     for j in range(N):
#         print(nums[(i, j)])


def count_upper(x, y, dx, dy):
    if 0 <= x + dx < N and 0 <= y + dy < N and nums[(x, y)] + 1 == nums[(x + dx, y + dy)]:
        return 1 + count_upper(x + dx, y + dy, dx, dy)
    return 1


def count_lower(x, y, dx, dy):
    if 0 <= x + dx < N and 0 <= y + dy < N and nums[(x, y)] - 1 == nums[(x + dx, y + dy)]:
        return 1 + count_lower(x + dx, y + dy, dx, dy)
    return 1


result_max = 0

for x in range(N):
    for y in range(N):
        result_max = max(result_max, count_upper(x, y, 1, 0))
        result_max = max(result_max, count_upper(x, y, 0, 1))
        result_max = max(result_max, count_upper(x, y, 1, 1))
        result_max = max(result_max, count_upper(x, y, 1, -1))
        result_max = max(result_max, count_lower(x, y, 1, 0))
        result_max = max(result_max, count_lower(x, y, 0, 1))
        result_max = max(result_max, count_lower(x, y, 1, 1))
        result_max = max(result_max, count_lower(x, y, 1, -1))

print(result_max)
