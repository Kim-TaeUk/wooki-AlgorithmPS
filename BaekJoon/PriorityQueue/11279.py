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
            print(hq.heappop(heap)[1])  # pop할 때는 우선순위([0]) 말고 값만 뽑기([1])
    else:
        # x가 크면 -x는 작아짐 -> -x를 우선순위로 써서 Max Heap을 구현
        hq.heappush(heap, (-x, x))
