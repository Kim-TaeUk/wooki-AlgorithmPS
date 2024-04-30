import sys
from collections import deque

N, M, R = map(int, sys.stdin.readline().split())
adjacent_list = [[] for _ in range(N + 1)]
distance = [-1 for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    adjacent_list[u].append(v)
    adjacent_list[v].append(u)

queue = deque()
queue.append(R)
distance[R] = 0
while queue:
    cur = queue.popleft()
    for nxt in adjacent_list[cur]:
        if distance[nxt] == -1:
            queue.append(nxt)
            distance[nxt] = distance[cur] + 1

print('\n'.join(map(str, distance[1:])))
