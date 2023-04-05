N = int(input())
n_list = [list(map(int, input().split())) for _ in range(N)]
M = int(input())

for i in range(M):
    h, t, k = map(int, input().split())

    if t == 0:  # 왼쪽 rotate
        for _ in range(k):
            n_list[h - 1].append(n_list[h - 1].pop(0))
    else:  # 오른쪽 rotate
        for _ in range(k):
            n_list[h - 1].insert(0, n_list[h - 1].pop())

res = 0
start = 0
end = N - 1

for i in range(N):
    for j in range(start, end + 1):
        res += n_list[i][j]
    if i < N // 2:
        start += 1
        end -= 1
    else:
        start -= 1
        end += 1

# <rotate하는 아이디어>
# 인덱스로 끊어서 이어붙이기 -> 내 아이디어
# pop해버리기 -> 해설 아이디어
