import sys

N = int(sys.stdin.readline().rstrip())

numbers = []
for _ in range(N):
    xi, yi = map(int, sys.stdin.readline().split())
    numbers.append((xi, yi))

numbers.sort(key=lambda x: (x[1], x[0]))

for xi, yi in numbers:
    print(xi, yi)
