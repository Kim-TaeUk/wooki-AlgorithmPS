"""
input
5
7
3 1
2 3
4 1
5 2
5 4
3 5
2 4
"""
import sys
from collections import deque


# Traversal in Connected Graph, BFS
def bfs():
    queue = deque()
    queue.append(2)  # start(BFS 시작점)
    visited[2] = True

    while queue:
        current = queue.popleft()
        for nxt in adjacent_list[current]:
            if visited[nxt]:
                continue
            queue.append(nxt)
            visited[nxt] = True  # visited check는 queue에 넣을 때!


V = int(sys.stdin.readline().rstrip())  # vertex (정점)
E = int(sys.stdin.readline().rstrip())  # edge (간선)
adjacent_list = [[] for _ in range(V + 1)]
for _ in range(E):
    start, end = map(int, sys.stdin.readline().split())
    adjacent_list[start].append(end)

visited = [False for _ in range(V + 1)]
bfs()
