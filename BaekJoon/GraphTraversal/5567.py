import sys
from collections import deque


def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        current = queue.popleft()
        for vertex in adj[current]:
            if not visited[vertex]:
                queue.append(vertex)
                visited[vertex] = True
                depth[vertex] = depth[current] + 1


N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())

adj = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
depth = [0 for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    adj[a].append(b)
    adj[b].append(a)

bfs(1)
print(sum(1 for x in depth if x == 1 or x == 2))
