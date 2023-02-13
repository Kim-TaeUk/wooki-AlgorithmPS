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

# 바깥 for문에서 i를 인덱스로, sum은 list[i]로, temp = i로
# 안에서 루프 돌리는데, sum < M이면 그냥 계속 도는게 기본 가정
# sum = M이면 cnt +1, while문 break
# sum > M이면 break
# sum < M이면 temp를 +1하고 temp가 가리키는 값까지 sum에 더해주면서 계속 돌게
