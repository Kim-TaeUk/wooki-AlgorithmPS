N = int(input())
n_list = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
m_list = [list(map(int, input().split())) for _ in range(M)]

res = 0

for i in range(M):
    if m_list[i][1] == 0:  # 왼
        left = n_list[(m_list[i][0] - 1)][:(N - m_list[i][2] + 1)]
        right = n_list[(m_list[i][0] - 1)][(N - m_list[i][2] + 1):]

        n_list[(m_list[i][0] - 1)] = right + left
    elif m_list[i][1] == 1:  # 오른
        left = n_list[(m_list[i][0] - 1)][:-m_list[i][2]]
        right = n_list[(m_list[i][0] - 1)][-m_list[i][2]:]

        n_list[(m_list[i][0] - 1)] = right + left

start = 0
end = N - 1
flag = 0
for i in range(N):
    for j in range(start, end + 1):
        res += n_list[i][j]
    if start == end:
        flag = 1
    if flag == 0:
        start += 1
        end -= 1
    else:
        start -= 1
        end += 1

print(res)
