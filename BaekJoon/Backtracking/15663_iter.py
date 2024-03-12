import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()

res = []
for i in permutations(lst, M):
    res.append(i)

res = sorted(list(set(res)))

for i in res:
    print(" ".join(map(str, i)))
