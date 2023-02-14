N = int(input())
myList = [list(map(int, input().split())) for _ in range(N)]

max = float('-inf')

for i in range(N):
    sum1 = sum2 = 0
    for j in range(N):
        sum1 += myList[i][j]  # 행의 합
        sum2 += myList[j][i]  # 열의 합
    if sum1 > max:
        max = sum1
    if sum2 > max:
        max = sum2

sum3 = sum4 = 0
for i in range(N):
    sum3 += myList[i][i]  # 우하향 대각 합
    sum4 += myList[i][N - i - 1]  # 좌하향 대각 합
if sum3 > max:
    max = sum3
if sum4 > max:
    max = sum4

# myList = [list(map(int, input().split())) for _ in range(N)]
# 2차원 배열을 한 줄 단위로 입력 받는 방법