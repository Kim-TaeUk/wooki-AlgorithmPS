import sys
from collections import deque


def bfs():
    queue = deque()
    queue.append(A)
    distance[A] = 0

    while queue:
        current = queue.popleft()
        for nxt in (current * 2, current + 1):
            if nxt == K:
                return distance[current] + 1
            if nxt > K:
                continue
            if distance[nxt] != -1:
                continue
            queue.append(nxt)
            distance[nxt] = distance[current] + 1


A, K = map(int, sys.stdin.readline().split())
distance = [-1 for _ in range(K)]

print(bfs())
