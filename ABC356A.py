N, L, R = map(int, input().split())
nums = [i+1 for i in range(N)]
L_idx = L - 1
R_idx = R - 1

for i in range(L_idx, L_idx + R_idx):
    if (i > R_idx - i + L_idx):
        break
    tmp = nums[i]
    nums[i] = nums[R_idx - i + L_idx]
    nums[R_idx - i + L_idx] = tmp
    # print("nums[{}]とnums[{}]を入れ替えました".format(i, R_idx-i + L_idx))

for num in nums:
    print(num, end=" ")
