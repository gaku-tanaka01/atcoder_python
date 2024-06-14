N = int(input())
cards = []

for i in range(2*N):
    tmp = int(input())
    cards.append(tmp)

positions = {i: [] for i in range(1, N+1)}

for i in range(len(cards)):
    positions[cards[i]].append(i)

# for i in range(N):
#     print(positions[cards[i]])

result = 0
for i in range(1, N+1):
    result += positions[i][1] - positions[i][0] - 1


print(result)
