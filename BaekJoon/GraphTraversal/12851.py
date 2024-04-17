from collections import deque
import sys

HUNDRED_THOUSAND = 100000
distance = [-1 for _ in range(HUNDRED_THOUSAND + 1)]
cnt = 0


def bfs(start, end):
    global cnt, distance
    queue = deque()
    queue.append(start)
    distance[start] = 0

    while queue:
        current = queue.popleft()
        if current == end:
            cnt += 1
        for nxt in (current - 1, current + 1, 2 * current):
            if nxt < 0 or nxt > HUNDRED_THOUSAND:
                continue
            # 동일한 탐색횟수를 가진 곳도 탐색해야한다!!
            if distance[nxt] == -1 or distance[nxt] == distance[current] + 1:
                queue.append(nxt)
                distance[nxt] = distance[current] + 1


N, K = map(int, sys.stdin.readline().split())
bfs(N, K)
print(distance[K])
print(cnt)
