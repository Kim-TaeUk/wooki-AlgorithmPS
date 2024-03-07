import sys
from collections import deque


def bfs(start_x, start_y, goal_x, goal_y):
    if start_x == goal_x and start_y == goal_y:
        return 0

    queue = deque()
    queue.append([start_x, start_y])
    board[start_x][start_y] = 0

    while queue:
        current_x, current_y = queue.popleft()

        for i in range(8):
            next_x, next_y = current_x + dx[i], current_y + dy[i]
            if next_x < 0 or next_x >= L or next_y < 0 or next_y >= L:
                continue

            if next_x == goal_x and next_y == goal_y:
                return board[current_x][current_y] + 1

            if board[next_x][next_y] == -1:
                board[next_x][next_y] = board[current_x][current_y] + 1
                queue.append([next_x, next_y])


dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    L = int(sys.stdin.readline().rstrip())
    from_x, from_y = map(int, sys.stdin.readline().split())
    to_x, to_y = map(int, sys.stdin.readline().split())
    board = [[-1 for _ in range(L)] for _ in range(L)]
    print(bfs(from_x, from_y, to_x, to_y))
