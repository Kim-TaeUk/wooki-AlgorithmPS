N = int(input())

cnt = 1  # 2를 미리 포함해서 1개
for i in range(3, N + 1):  # i를 3부터 N까지
    flag = 0
    for j in range(2, i):  # 나누려는 수는 2부터 i-1까지
        if i % j == 0:  # 나누어떨어지면
            flag += 1  # cnt 1 증가
    # i-1까지 나누어 보고
    if flag == 0:  # cnt=0이면 -> 한 번도 나누어떨어지지 않았다면
        cnt += 1  # 개수 하나 늘려줌

print(cnt)
