import sys

N = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().rstrip())

prefixsum = [0]
tmp = 0
for number in numbers:
    tmp += number
    prefixsum.append(tmp)

for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    print(prefixsum[end] - prefixsum[start - 1])
