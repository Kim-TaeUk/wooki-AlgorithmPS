T = int(input())

for times in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    res = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            tmp = 0
            for s in range(i, i + M):
                for e in range(j, j + M):
                    tmp += arr[s][e]
            if res < tmp:
                res = tmp

    print("#", end="")
    print((times + 1), res)
