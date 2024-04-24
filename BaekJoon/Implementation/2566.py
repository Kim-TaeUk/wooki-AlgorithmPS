import sys

mx = -1
rx, ry = -1, -1
for i in range(9):
    lst = list(map(int, sys.stdin.readline().split()))
    if max(lst) > mx:
        mx = max(lst)
        rx = i + 1
        ry = lst.index(mx) + 1

print(mx)
print(rx, ry)
