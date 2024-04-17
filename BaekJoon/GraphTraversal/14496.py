import sys
from collections import deque


def bfs(s, e):
    global distance
    queue = deque()
    queue.append(s)
    distance[s] = 0

    while queue:
        current = queue.popleft()
        for nxt in adj[current]:
            if distance[nxt] == -1:
                queue.append(nxt)
                distance[nxt] = distance[current] + 1

    if distance[e] == -1:
        return -1
    else:
        return distance[e]


a, b = map(int, sys.stdin.readline().split())
N, M = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(N + 1)]
distance = [-1 for _ in range(N + 1)]
for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    adj[start].append(end)
    adj[end].append(start)

print(bfs(a, b))
