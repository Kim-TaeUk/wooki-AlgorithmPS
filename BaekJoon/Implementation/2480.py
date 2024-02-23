import sys

x, y, z = map(int, sys.stdin.readline().split())

if x == y == z:
    print(10000 + x * 1000)
elif x == y or y == z or z == x:
    if x == y:
        print(1000 + x * 100)
    elif y == z:
        print(1000 + y * 100)
    else:
        print(1000 + z * 100)
else:
    print(max(x, y, z) * 100)
