"""
input
6
4
1 2
1 3
2 4
5 6
"""
import sys
from collections import deque


# Traversal in not Connected Graph, BFS
def bfs(start_v):
    queue = deque()
    queue.append(start_v)  # start(BFS 시작점)
    visited[start_v] = True

    while queue:
        current = queue.popleft()
        for nxt in adjacent_list[current]:
            if visited[nxt]:
                continue
            queue.append(nxt)
            visited[nxt] = True


V = int(sys.stdin.readline().rstrip())  # vertex (정점)
E = int(sys.stdin.readline().rstrip())  # edge (간선)
adjacent_list = [[] for _ in range(V + 1)]
for _ in range(E):
    start, end = map(int, sys.stdin.readline().split())
    adjacent_list[start].append(end)
    adjacent_list[end].append(start)

visited = [False for _ in range(V + 1)]
for v in range(1, V + 1):  # for 문으로 방문하지 않은 vertex 찾아서 BFS 시작
    if visited[v]:
        continue
    bfs(v)
