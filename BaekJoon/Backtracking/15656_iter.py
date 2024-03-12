import sys
from itertools import product

N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()

for i in product(lst, repeat=M):
    print(" ".join(map(str, i)))
