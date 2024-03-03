import sys
import heapq as hq

N = int(sys.stdin.readline().rstrip())
heap = []
for _ in range(N):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        if heap:
            print(hq.heappop(heap)[1])
        else:
            print(0)
    else:
        hq.heappush(heap, (abs(x), x))
