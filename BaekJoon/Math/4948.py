import sys

MAX = 10 * 2
prime_num = [i for i in range(MAX + 1)]
prime_num[1] = 0
for i in range(2, int(MAX ** 0.5) + 1):
    if prime_num[i] == 0:
        continue
    for j in range(i * i, MAX + 1, i):
        prime_num[j] = 0

while True:
    N = int(sys.stdin.readline().rstrip())
    if N == 0:
        break
    print(sum([1 for i in prime_num[N + 1:2 * N + 1] if prime_num[i]]))
