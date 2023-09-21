import sys

N = int(sys.stdin.readline().rstrip())

area = []
for _ in range(N):
    xpoint, ypoint = map(int, sys.stdin.readline().split())
    area.append((xpoint, ypoint))

area.sort(key=lambda x: (x[0], x[1]))

for xpoint, ypoint in area:
    print(xpoint, ypoint)
