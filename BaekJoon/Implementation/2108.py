import sys
from collections import Counter

N = int(sys.stdin.readline().strip())
numbers = sorted([int(sys.stdin.readline().rstrip()) for _ in range(N)])

if sum(numbers) > 0:
    print(int(sum(numbers) / N + 0.5))
else:
    print(int(sum(numbers) / N - 0.5))

print(numbers[N // 2])

counts = Counter(numbers)
max_count = max(counts.values())
freqvalue = [item for item, count in counts.items() if count == max_count]

if len(freqvalue) > 1:
    print(freqvalue[1])
else:
    print(freqvalue[0])

print(max(numbers) - min(numbers))
