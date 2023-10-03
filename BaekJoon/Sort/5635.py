import sys

n = int(sys.stdin.readline().rstrip())
lst = []
for _ in range(n):
    name, day, month, year = map(str, sys.stdin.readline().split())
    lst.append((name, int(day), int(month), int(year)))

lst.sort(key=lambda x: (x[3], x[2], x[1]))
print(lst[-1][0])
print(lst[0][0])
