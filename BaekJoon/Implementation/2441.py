import sys

N = int(sys.stdin.readline().rstrip())

for times in range(N, 0, -1):
    print(" " * (N - times), end="")
    print("*" * times)
