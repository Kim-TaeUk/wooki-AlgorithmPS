N = int(input())
input_list = [list(map(int, input().split())) for _ in range(N)]
n_list = [[0] * (N + 2) for _ in range(N + 2)]

for i in range(N):
    for j in range(N):
        n_list[i + 1][j + 1] = input_list[i][j]

cnt = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if n_list[i][j] < n_list[i - 1][j]:
            continue
        elif n_list[i][j] < n_list[i + 1][j]:
            continue
        elif n_list[i][j] < n_list[i][j - 1]:
            continue
        elif n_list[i][j] < n_list[i][j + 1]:
            continue
        cnt += 1

print(cnt)
