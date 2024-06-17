from collections import deque
M, N= map(int, input().split())
maze = [None] * N
for i in range(N):
    maze[i] = input().split()

        
for i in range(N):
    for j in range(M):
        if maze[i][j] == "s":
            start = (i, j)
        if maze[i][j] == "g":
            goal = (i, j)

# print(start, goal)

distance = {}
distance[start] = 0
proceeds = [(0, 1), (1, 0), (0, -1), (-1, 0)]
next_step = deque()
visited_position = set(start)
next_step.append(start)

while next_step:
    current = next_step.popleft()
    for proceed in proceeds:
        next_position = (current[0] + proceed[0], current[1] + proceed[1])
        if next_position[0] in range(N) and next_position[1] in range(M) and maze[next_position[0]][next_position[1]] != "1" and not next_position in visited_position:
            # print(next_position)
            next_step.append(next_position)
            distance[next_position] = distance[current] + 1
            visited_position.add(next_position)


if goal in distance:
    print(distance[goal])
else:
    print("Fail")

