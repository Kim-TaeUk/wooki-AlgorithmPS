n = int(input())
n_list = [list(map(int, input().split())) for _ in range(n)]

n_list.sort(key=lambda x: (x[1], x[0]))

cnt = 1
cur = n_list[0][1]

for i in range(n):
    if cur <= n_list[i][0]:
        cur = n_list[i][1]
        cnt += 1

print(cnt)
