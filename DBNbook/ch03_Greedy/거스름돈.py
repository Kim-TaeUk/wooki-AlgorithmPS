import sys

N = int(sys.stdin.readline().rstrip())
coin_types = [500, 100, 50, 10]
count = 0

for coin in coin_types:
    count += N / coin
    N %= count

print(count)
