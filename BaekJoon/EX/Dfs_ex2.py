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


# Traversal in Connected Graph, recursive DFS
def dfs(current):
    visited[current] = True
    for nxt in adjacent_list[current]:
        if visited[nxt]:
            continue
        dfs(nxt)


V = int(sys.stdin.readline().rstrip())  # vertex (정점)
E = int(sys.stdin.readline().rstrip())  # edge (간선)
adjacent_list = [[] for _ in range(V + 1)]
for _ in range(E):
    start, end = map(int, sys.stdin.readline().split())
    adjacent_list[start].append(end)
    adjacent_list[end].append(start)

visited = [False for _ in range(V + 1)]
dfs(2)  # start(DFS 시작점)
