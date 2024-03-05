import sys
import heapq as hq

N = int(sys.stdin.readline().rstrip())
heap = []
for i in range(N):
    numbers = list(map(int, sys.stdin.readline().split()))
    if i == 0:
        for number in numbers:
            hq.heappush(heap, number)
    else:
        for number in numbers:
            if heap[0] < number:
                hq.heappush(heap, number)
                hq.heappop(heap)

print(heap[0])
