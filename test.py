import random

N, M = 100, 100  # 行数と列数
maze = [['0' for _ in range(M)] for _ in range(N)]

# スタートとゴールの位置をランダムに設定
start_x, start_y = random.randint(0, N-1), random.randint(0, M-1)
goal_x, goal_y = random.randint(0, N-1), random.randint(0, M-1)
maze[start_x][start_y] = 's'
maze[goal_x][goal_y] = 'g'

# 壁（'1'）をランダムに配置、迷路の30%を壁にする
num_walls = (N * M) * 30 // 100
for _ in range(num_walls):
    x, y = random.randint(0, N-1), random.randint(0, M-1)
    if (x, y) != (start_x, start_y) and (x, y) != (goal_x, goal_y):
        maze[x][y] = '1'

# 迷路の出力
print(N, M)
for row in maze:
    print(' '.join(row))
