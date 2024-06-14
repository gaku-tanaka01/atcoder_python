N, Y = list(map(int, input().split()))


def is_exist(Y):
    co_m = 0
    co_k5 = 0
    co_k = 0

    for i in range(N):
        if (Y - 10000 >= 0):
            co_m += 1
            Y -= 10000
        else:
            break

    for i in range(N-co_m):
        if (Y - 5000 >= 0):
            co_k5 += 1
            Y -= 5000
        else:
            break

    for i in range(N-co_k5-co_m):
        if (Y - 1000 >= 0):
            co_k += 1
            Y -= 1000
        else:
            break
    print(co_m, co_k5, co_k)
    if (10000*co_m + 5000*co_k5 + 1000*co_k == Y):
        return [co_m, co_k5, co_k]
    else:
        return [-1, -1, -1]


result = is_exist(Y)


print(" ".join(map(str, result)))
