import heapq as hq

lst = []
while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(lst) == 0:
            print(-1)
        else:
            print(-hq.heappop(lst))
    else:
        hq.heappush(lst, -n)
