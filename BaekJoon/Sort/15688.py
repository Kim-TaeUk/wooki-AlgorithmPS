import sys

N = int(sys.stdin.readline().rstrip())
lst = []
for _ in range(N):
    lst.append(int(sys.stdin.readline().rstrip()))

lst.sort()
for x in lst:
    print(x)
