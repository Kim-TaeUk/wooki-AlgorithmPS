import sys
from collections import Counter

N = int(sys.stdin.readline().rstrip())
lst = []
for _ in range(N):
    lst.append(int(sys.stdin.readline().rstrip()))

res = sorted(Counter(lst).most_common(), key=lambda x: (-x[1], x[0]))
print(res[0][0])
