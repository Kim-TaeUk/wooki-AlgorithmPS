import sys
import heapq as hq

N = int(sys.stdin.readline().rstrip())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline().rstrip()))

hq.heapify(arr)
ans = 0

while len(arr) > 1:
    a = hq.heappop(arr)
    b = hq.heappop(arr)
    ans += a + b
    hq.heappush(arr, a + b)

print(ans)
