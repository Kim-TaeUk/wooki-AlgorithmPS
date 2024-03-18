import sys

N = int(sys.stdin.readline().rstrip())
lst = [0 for _ in range(2000001)]
for _ in range(N):
    lst[int(sys.stdin.readline().rstrip()) + 1000000] += 1

for i in range(len(lst)):
    if lst[i] != 0:
        while lst[i] != 0:
            print(i - 1000000)
            lst[i] -= 1
