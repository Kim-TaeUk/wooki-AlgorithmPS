import sys

N, M = map(int, sys.stdin.readline().split())
bulbs = list(map(int, sys.stdin.readline().split()))

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())

    if a == 1:
        bulbs[b - 1] = c
    elif a == 2:
        for i in range(b - 1, c):
            if bulbs[i] == 0:
                bulbs[i] = 1
            else:
                bulbs[i] = 0
    elif a == 3:
        bulbs[b - 1:c] = [0] * (c - b + 1)
    elif a == 4:
        bulbs[b - 1:c] = [1] * (c - b + 1)

for bulb in bulbs:
    print(bulb, end=" ")
