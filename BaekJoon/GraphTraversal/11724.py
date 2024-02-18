from collections import deque
import sys


def bfs(start_v):
    queue = deque()
    queue.append(start_v)
    visited[start_v] = True

    while queue:
        current_v = queue.popleft()

        for next_v in adj[current_v]:
            if not visited[next_v]:
                queue.append(next_v)
                visited[next_v] = True


N, M = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    adj[start].append(end)
    adj[end].append(start)

visited = [False] * (N + 1)
res = 0
for i in range(1, N + 1):
    if not visited[i]:
        bfs(i)
        res += 1

print(res)
