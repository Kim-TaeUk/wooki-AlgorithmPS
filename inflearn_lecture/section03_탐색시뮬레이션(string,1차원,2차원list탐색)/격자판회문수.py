input_list = [list(map(int, input().split())) for _ in range(7)]

cnt = 0
for i in range(7):
    for j in range(3):
        if input_list[i][j] == input_list[i][j + 4] and input_list[i][j + 1] == input_list[i][j + 3]:
            cnt += 1

for j in range(7):
    for i in range(3):
        if input_list[i][j] == input_list[i + 4][j] and input_list[i + 1][j] == input_list[i + 3][j]:
            cnt += 1

print(cnt)
