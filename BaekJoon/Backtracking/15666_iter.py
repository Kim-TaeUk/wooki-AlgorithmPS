import sys
from itertools import combinations_with_replacement

N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()

res = []
for i in combinations_with_replacement(lst, M):
    res.append(i)

res = sorted(list(set(res)))

for i in res:
    print(" ".join(map(str, i)))
