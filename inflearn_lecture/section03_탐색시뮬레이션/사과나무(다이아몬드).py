N = int(input())
list = [list(map(int, input().split())) for _ in range(N)]

sum = 0
k = N // 2
start = end = k

for i in range(N):
    for j in range(start, end + 1):
        sum += list[i][j]
    if i < k:
        start -= 1
        end += 1
    else:
        start += 1
        end -= 1
