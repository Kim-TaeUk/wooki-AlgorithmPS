import sys

N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

prefixsum = [0] * (N + 1)
for i in range(N):
    prefixsum[i + 1] = prefixsum[i] + numbers[i]

for _ in range(M):
    left, right = map(int, sys.stdin.readline().split())
    print(prefixsum[right] - prefixsum[left - 1])
