import sys

N = int(sys.stdin.readline().rstrip())

cnt = 0
cows = [-1] * 11

for _ in range(N):
    number, location = map(int, sys.stdin.readline().split())

    if cows[number] == -1:
        cows[number] = location
    elif cows[number] != location:
        cows[number] = location
        cnt += 1

print(cnt)

# 2차원 배열 사용X -> 개선
# 1차원 배열 사용 -> 메모리 효율적
