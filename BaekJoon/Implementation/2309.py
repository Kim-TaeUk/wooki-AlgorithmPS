import sys
from itertools import combinations

dwarf = []
for _ in range(9):
    dwarf.append(int(sys.stdin.readline().rstrip()))

for i in combinations(dwarf, 7):
    if sum(i) == 100:
        print("\n".join(map(str, sorted(i))))
        break
