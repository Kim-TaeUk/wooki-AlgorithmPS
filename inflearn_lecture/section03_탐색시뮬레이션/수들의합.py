N, M = map(int, input().split())
list = list(map(int, input().split()))
cnt = 0

for i in range(N):
    sum = list[i]
    temp = i

    while True:
        if sum == M:
            cnt += 1
            break
        if sum > M:
            break

        if temp == N - 1:
            break
        temp += 1
        sum += list[temp]

print(cnt)
