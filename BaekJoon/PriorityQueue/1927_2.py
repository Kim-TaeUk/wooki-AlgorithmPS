import sys
import heapq as hq

N = int(sys.stdin.readline().rstrip())
heap = []
for _ in range(N):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        if not heap:
            print(0)
        else:
            print(hq.heappop(heap))
    else:
        hq.heappush(heap, x)
