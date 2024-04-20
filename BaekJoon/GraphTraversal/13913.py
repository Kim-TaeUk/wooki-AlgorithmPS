from collections import deque
import sys

HUNDRED_THOUSAND = 100000


def bfs(start, end):
    global distance, path, prev
    queue = deque()

    queue.append(start)
    distance[start] = 0

    while queue:
        current = queue.popleft()
        if current == end:
            # 도착점 -> 시작점, 역으로 추적 - path에 넣기
            while current != -1:  # 시작점은 이전 좌표가 없으니 -1
                path.append(current)
                current = prev[current]  # 이전 좌표로 갱신
            return distance[end]

        for nextn in (current - 1, current + 1, 2 * current):
            if 0 <= nextn <= HUNDRED_THOUSAND and distance[nextn] == -1:
                queue.append(nextn)
                distance[nextn] = distance[current] + 1
                prev[nextn] = current  # prev에는 이전 좌표를 저장한다


N, K = map(int, sys.stdin.readline().split())
distance = [-1 for _ in range(HUNDRED_THOUSAND + 1)]
prev = [-1 for _ in range(HUNDRED_THOUSAND + 1)]
path = []
print(bfs(N, K))
print(*path[::-1])
