import sys
from itertools import combinations_with_replacement

N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()

for i in combinations_with_replacement(lst, M):
    print(" ".join(map(str, i)))
