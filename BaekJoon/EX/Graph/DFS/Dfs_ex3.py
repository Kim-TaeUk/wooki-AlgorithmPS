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


# Traversal in Connected Graph, non-recursive DFS
# ex1처럼 non-recursive한 방식이지만,
# stack에 넣을 때가 아니라 뺄 때 visited check하는 방식으로
# 관념적인 DFS처럼 동작하도록
def dfs():
    stack = []
    stack.append(2)  # start(DFS 시작점)
    # visited[2] = True

    while stack:
        current = stack.pop()
        if visited[current]:
            continue
        visited[current] = True
        for nxt in adjacent_list[current]:
            if visited[nxt]:
                continue
            stack.append(nxt)
            # visited[nxt] = True


V = int(sys.stdin.readline().rstrip())  # vertex (정점)
E = int(sys.stdin.readline().rstrip())  # edge (간선)
adjacent_list = [[] for _ in range(V + 1)]
for _ in range(E):
    start, end = map(int, sys.stdin.readline().split())
    adjacent_list[start].append(end)
    adjacent_list[end].append(start)

visited = [False for _ in range(V + 1)]
dfs()
