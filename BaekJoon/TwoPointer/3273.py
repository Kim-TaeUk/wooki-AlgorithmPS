import sys

n = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline().rstrip())

lst.sort()
res = 0
lt = 0
rt = n - 1

while lt < rt:
    if lst[lt] + lst[rt] == x:
        lt += 1
        rt -= 1
        res += 1
    elif lst[lt] + lst[rt] > x:
        rt -= 1
    elif lst[lt] + lst[rt] < x:
        lt += 1

print(res)
