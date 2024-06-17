S = input()
T = input()
counter = 0
result = []
for i in range(len(S)):
    for j in range(counter, len(T)):
        if T[j] == S[i]:
            result.append(j + 1)
            counter = j + 1
            break
for i in range(len(result)):
    print(result[i], end=" ")
