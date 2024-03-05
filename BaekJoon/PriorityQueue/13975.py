import sys
import heapq as hq

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    K = int(sys.stdin.readline().rstrip())
    files = list(map(int, sys.stdin.readline().split()))

    hq.heapify(files)
    ans = 0
    while len(files) > 1:
        a = hq.heappop(files)
        b = hq.heappop(files)
        ans += a + b
        hq.heappush(files, a + b)
    print(ans)
