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

# sum은 lt ~ rt-1의 부분합 -> list[0]으로 초기화시켜놓음 일단
# sum < M이면 rt를 한 칸 뒤로 넘기고, rt까지 sum에 추가
# 근데 sum < M이어도 rt가 N보다 같거나 커버리면 while문 탈출하게

# sum = M이면 cnt +1, sum에서 lt가 가리키는 값 빼고 lt는 한 칸 뒤로 넘기고

# sum > M이면 sum에서 lt가 가리키는 값 빼고 lt는 한 칸 뒤로 넘기고
