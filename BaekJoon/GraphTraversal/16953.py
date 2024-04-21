import sys
from collections import deque


def bfs():
    queue = deque()
    queue.append([A, 0])

    while queue:
        current, distance = queue.popleft()
        if current == B:
            return distance + 1

        for nxt in (2 * current, 10 * current + 1):
            if nxt > B:
                continue
            queue.append([nxt, distance + 1])
    return -1


A, B = map(int, sys.stdin.readline().split())
print(bfs())
