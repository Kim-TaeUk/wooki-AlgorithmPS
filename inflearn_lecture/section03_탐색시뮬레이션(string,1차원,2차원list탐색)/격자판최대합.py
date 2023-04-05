N = int(input())
myList = [0 for _ in range(N)]
for i in range(N):
    myList[i] = list(map(int, input().split()))

max = 0

# 가로 합 N개
for i in range(N):
    sum = 0
    for j in range(N):
        sum += myList[i][j]

    if max < sum:
        max = sum

# 세로 합 N개
for i in range(N):
    sum = 0
    for j in range(N):
        sum += myList[j][i]

    if max < sum:
        max = sum

# 우하향 대각 합 1개
sum = 0
for i in range(N):
    sum += myList[i][i]

if max < sum:
    max = sum

# 좌하향 대각 합 1개
sum = 0
for i in range(N):
    sum += myList[N - 1 - i][i]

if max < sum:
    max = sum

print(max)
