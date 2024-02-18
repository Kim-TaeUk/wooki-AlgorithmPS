from collections import deque
import sys


def bfs(start, end):
    queue = deque()
    visited = [-1] * 100001

    queue.append(start)
    visited[start] = 0

    while queue:
        current = queue.popleft()
        if current == end:
            return visited[end]

        for nextn in (current - 1, current + 1, 2 * current):
            if 0 <= nextn <= 100000 and visited[nextn] == -1:
                queue.append(nextn)
                visited[nextn] = visited[current] + 1


N, K = map(int, sys.stdin.readline().split())
print(bfs(N, K))
