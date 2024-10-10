from itertools import combinations
import sys

N, K = map(int, sys.stdin.readline().split())
houses = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

res = float('inf')
for candidate in combinations(houses, K):
    tmp = float('-inf')
    for house in houses:
        k = float('inf')
        flag = True
        for i in range(K):
            distance = abs(house[0] - candidate[i][0]) + abs(house[1] - candidate[i][1])
            if distance == 0:
                flag = False
                break
            else:
                k = min(k, distance)
        if flag:
            tmp = max(tmp, k)
    res = min(tmp, res)

print(res)
