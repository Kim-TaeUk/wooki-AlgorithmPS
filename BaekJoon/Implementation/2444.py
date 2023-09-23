import sys

N = int(sys.stdin.readline().rstrip())

for times in range(1, N):
    print(' ' * (N - times) + '*' * (2 * times - 1))
for times in range(N, 0, -1):
    print(' ' * (N - times) + '*' * (2 * times - 1))
