import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

cost = [[float('inf') for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(n + 1):
    cost[i][i] = 0

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    cost[a][b] = min(cost[a][b], c)

for k in range(n + 1):
    for i in range(n + 1):
        for j in range(n + 1):
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if cost[i][j] == float('inf'):
            print(0, end=" ")
        else:
            print(cost[i][j], end=" ")
    print()
