import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

lst.sort()
for i in combinations(lst, M):
    print(" ".join(map(str, i)))
