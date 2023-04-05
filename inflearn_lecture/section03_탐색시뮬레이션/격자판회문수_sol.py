input_list = [list(map(int, input().split())) for _ in range(7)]

cnt = 0
for i in range(3):  # 가로일 때 판별
    for j in range(7):
        tmp = input_list[j][i:i + 5]
        if tmp == tmp[::-1]:
            cnt += 1

        for k in range(2):  # 세로일 때 판별
            if input_list[i + k][j] != input_list[i + 5 - k - 1][j]:
                break
            else:
                cnt += 1
print(cnt)

# slicing으로 가로 해결
# for - else와 인덱스 조작해서 세로 해결
