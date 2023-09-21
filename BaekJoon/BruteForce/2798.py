import sys

N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

sums = set()

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            if numbers[i] + numbers[j] + numbers[k] <= M:
                sums.add(numbers[i] + numbers[j] + numbers[k])

print(max(list(sums)))
