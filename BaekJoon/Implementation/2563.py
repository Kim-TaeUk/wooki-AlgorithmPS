import sys

board = [[0 for _ in range(100)] for _ in range(100)]

N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            board[i][j] = 1

res = 0
for row in board:
    res += row.count(1)
print(res)
