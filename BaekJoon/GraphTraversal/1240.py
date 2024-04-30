import sys
from collections import deque


def bfs(start, end):
    queue = deque()
    queue.append([start, 0])
    visited = [False for _ in range(N + 1)]
    visited[start] = True

    while queue:
        current, distance = queue.popleft()
        if current == end:
            return distance
        for nxt, distnce in adjacent_list[current]:
            if not visited[nxt]:
                visited[nxt] = True
                queue.append([nxt, distnce + distance])


N, M = map(int, sys.stdin.readline().split())
adjacent_list = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v, dist = map(int, sys.stdin.readline().split())
    adjacent_list[u].append([v, dist])
    adjacent_list[v].append([u, dist])
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    print(bfs(u, v))
