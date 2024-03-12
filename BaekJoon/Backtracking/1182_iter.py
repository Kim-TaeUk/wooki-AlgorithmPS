import sys
from itertools import combinations

N, S = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

cnt = 0
for i in range(1, N + 1):
    for x in combinations(lst, i):
        if sum(x) == S:
            cnt += 1

print(cnt)
