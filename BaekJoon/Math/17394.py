import sys
from collections import deque

MILLION = 1000000
HUNDRED_THOUSAND = 100000


def snap(total, start, end):
    distance = [-1 for _ in range(MILLION + 1)]
    queue = deque()
    queue.append(total)
    distance[total] = 0

    while queue:
        current = queue.popleft()
        if start <= current <= end:
            if sieve[current]:
                return distance[current]

        next_step = [current // 2, current // 3, current + 1, current - 1]
        for nxt in next_step:
            if 0 <= nxt <= MILLION and distance[nxt] == -1:
                distance[nxt] = distance[current] + 1
                queue.append(nxt)
    return -1


sieve = [True for _ in range(HUNDRED_THOUSAND + 1)]
sieve[0], sieve[1] = False, False
for i in range(2, int(HUNDRED_THOUSAND ** 0.5) + 1):
    if sieve[i]:
        j = 2
        while i * j <= HUNDRED_THOUSAND:
            sieve[i * j] = False
            j += 1

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    N, A, B = map(int, sys.stdin.readline().split())
    print(snap(N, A, B))
