import sys

N = int(sys.stdin.readline().rstrip())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
lst.sort(key=lambda x: (x[1], x[0]))

cnt, cur_time = 0, 0

for x in lst:
    if cur_time > x[0]:
        continue
    cur_time = x[1]
    cnt += 1

print(cnt)

# 회의의 시작 시간 = 종료 시간일 때 고려하지 않는 것 유의
