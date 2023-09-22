import sys

N = int(sys.stdin.readline().rstrip())

cnt = 0
cows = [[x + 1, -1] for x in range(10)]

for _ in range(N):
    number, location = map(int, sys.stdin.readline().split())

    if cows[number - 1][1] != location and cows[number - 1][1] != -1:
        cnt += 1
        cows[number - 1][1] = location
    else:
        cows[number - 1][1] = location

print(cnt)
