import sys

N = int(sys.stdin.readline().rstrip())

for times in range(N - 1, -1, -1):
    print(" " * times, end="")
    print("*" * (2 * (N - times) - 1))
