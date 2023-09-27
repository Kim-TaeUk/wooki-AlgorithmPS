import sys


def dfs(current):
    global cnt

    cnt += 1
    visited[current] = 1

    for com in adj[current]:
        if visited[com] == 0:
            dfs(com)


N = int(sys.stdin.readline().rstrip())
pairs = int(sys.stdin.readline().rstrip())

adj = [[] for _ in range(N + 1)]

for _ in range(pairs):
    com1, com2 = map(int, sys.stdin.readline().split())
    adj[com1].append(com2)
    adj[com2].append(com1)

cnt = 0
visited = [0] * (N + 1)
dfs(1)
print(cnt - 1)
