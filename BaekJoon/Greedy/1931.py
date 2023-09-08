n = int(input())
n_list = [list(map(int, input().split())) for _ in range(n)]

n_list.sort(key=lambda x: (x[1], x[0]))

cnt = 0
cur = 0

for i in range(n):
    if cur <= n_list[i][0]:
        cur = n_list[i][1]
        cnt += 1

print(cnt)

# 회의의 시작 시간 = 종료 시간일 때 고려하지 않은 풀이여서 틀렸었음
# cnt = 0, cur = 0으로 바꿔주거나
# cnt = 1, cur = n_list[0][1] 그대로에 for문을 range(1, n)으로 주면 됨
