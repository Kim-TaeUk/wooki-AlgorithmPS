N = int(input())
input_list = [list(map(int, input().split())) for _ in range(N)]

# 이걸로 상하좌우 조정
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 가장자리 0으로 채우기
input_list.insert(0, [0] * N)
input_list.append([0] * N)
for x in input_list:
    x.insert(0, 0)
    x.append(0)

cnt = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if all(input_list[i][j] > input_list[i + dx[k]][j + dy[k]] for k in range(4)):
            cnt += 1

print(cnt)

# dx, dy 도입해서 상하좌우 k로 range조정하면서 확인하는 아이디어
# 가장자리 채우는 아이디어 나랑 다름 - '곳감' 문제처럼 insert, append만 이용해서 해결하는 아이디어
# all을 이용하는 아이디어
