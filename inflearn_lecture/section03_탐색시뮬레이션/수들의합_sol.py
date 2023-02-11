N, M = map(int, input().split())
list = list(map(int, input().split()))

lt = 0
rt = 1
sum = list[0]
cnt = 0

while True:
    if sum < M:
        if rt < N:
            sum += list[rt]
            rt += 1
        else:
            break
    elif sum == M:
        cnt += 1
        sum -= list[lt]
        lt += 1
    else:
        sum -= list[lt]
        lt += 1

print(cnt)
