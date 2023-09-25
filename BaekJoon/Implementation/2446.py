import sys

N = int(sys.stdin.readline().rstrip())

for times in range(1, N + 1):
    print(" " * (times - 1) + "*" * (2 * (N - times) + 1))
for times in range(1, N):
    print(" " * (N - times - 1) + "*" * (2 * times + 1))
