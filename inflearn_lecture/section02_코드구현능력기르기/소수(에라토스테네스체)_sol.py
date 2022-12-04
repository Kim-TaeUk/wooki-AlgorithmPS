N = int(input())

list = [0] * (N + 1)

# k=[]
cnt = 0
for i in range(2, N + 1):  # 2부터 N까지 도는데
    if list[i] == 0:  # list[i]가 0이면 -> 0이 아니면 아래 for문은 돌지도 않음
        cnt += 1  # 개수 하나 세고
        # k.append(i)
        for j in range(i, N + 1, i):  # 배수들 다 1로 바꿔버림
            list[j] = 1

print(cnt)
# print(k)
