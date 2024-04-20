import sys
from collections import deque

HUNDRED_THOUSAND = 100000


def bfs(start, end):
    global distance
    queue = deque()

    queue.append(start)
    distance[start] = 0

    while queue:
        current = queue.popleft()
        if current == end:
            return distance[end]

        for nextn in (2 * current, current - 1, current + 1):
            if nextn < 0 or nextn > HUNDRED_THOUSAND:
                continue
            if distance[nextn] == -1:
                if nextn == 2 * current:
                    queue.append(nextn)
                    distance[nextn] = distance[current]
                else:
                    queue.append(nextn)
                    distance[nextn] = distance[current] + 1


N, K = map(int, sys.stdin.readline().split())
distance = [-1 for _ in range(HUNDRED_THOUSAND + 1)]
print(bfs(N, K))
