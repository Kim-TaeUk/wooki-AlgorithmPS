import sys
import heapq as hq

N = int(sys.stdin.readline().rstrip())
min_heap = []
max_heap = []
for _ in range(N):
    num = int(sys.stdin.readline().rstrip())

    if len(min_heap) == len(max_heap):
        hq.heappush(max_heap, (-num, num))
    else:
        hq.heappush(min_heap, num)

    if max_heap and min_heap and min_heap[0] < max_heap[0][1]:
        min_heap_root = hq.heappop(min_heap)
        max_heap_root = hq.heappop(max_heap)[1]

        hq.heappush(min_heap, max_heap_root)
        hq.heappush(max_heap, (-min_heap_root, min_heap_root))

    print(max_heap[0][1])

'''
시간 제한 0.1초
max heap 1개, min heap 1개 -> heap 2개로 풀이

1. min heap과 max heap에 번갈아 가며 채워준다(시작은 max heap부터)
2. max heap의 root >= min heap의 root
-> min heap의 root < max heap의 root인 경우 둘을 swap

2가지 조건을 만족하면 중간 값은 max heap의 root이다 
'''
