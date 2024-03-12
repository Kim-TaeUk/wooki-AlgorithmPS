import sys
from itertools import product

N, M = map(int, sys.stdin.readline().split())

lst = [i for i in range(1, N + 1)]
for i in product(lst, repeat=M):
    print(" ".join(map(str, i)))
