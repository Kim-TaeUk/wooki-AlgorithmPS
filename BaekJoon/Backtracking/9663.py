import sys


def func(cur):  # cur번째 row에 queen 배치
    global cnt
    if cur == N:
        cnt += 1
        return

    for i in range(N):  # (cur, i)에 queen 배치
        if is_used1[i] or is_used2[i + cur] or is_used3[cur - i + N - 1]:
            continue

        is_used1[i] = True
        is_used2[i + cur] = True
        is_used3[cur - i + N - 1] = True
        func(cur + 1)
        is_used1[i] = False
        is_used2[i + cur] = False
        is_used3[cur - i + N - 1] = False


N = int(sys.stdin.readline().rstrip())
cnt = 0
is_used1 = [False] * (N + 1)  # y
is_used2 = [False] * (2 * N - 1)  # x + y: / 방향 대각선
is_used3 = [False] * (2 * N - 1)  # x - y + (N - 1): \ 방향 대각선
func(0)
print(cnt)
