import sys

N = int(sys.stdin.readline().rstrip())

for times in range(1, N + 1):
    print("*" * times + " " * 2 * (N - times) + "*" * times)
for times in range(1, N):
    print("*"* (N - times) + " " * 2 * times + "*" * (N - times))
