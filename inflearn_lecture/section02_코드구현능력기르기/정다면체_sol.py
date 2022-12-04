N, M = map(int, input().split())

cnt = [0] * (N + M + 1)

for i in range(1, N + 1):
    for j in range(1, M + 1):
        cnt[i + j] += 1  # 두 수의 합을 cnt의 인덱스로 생각하고 값을 키워주는 방식으로
        # -> 가장 큰 값이 확률이 가장 높은 숫자

max = float('-inf')
for i in range(N + M + 1):  # 최대값 찾고
    if cnt[i] > max:
        max = cnt[i]

for i in range(N + M + 1):  # 최대값인거 출력
    if cnt[i] == max:
        print(i, end=' ')
