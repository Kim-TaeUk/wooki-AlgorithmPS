import sys

N = int(sys.stdin.readline().rstrip())

# dp[i] = i를 1로 만들기 위해 필요한 연산 사용 횟수의 최소값
dp = [0 for _ in range(N + 1)]
dp[1] = 0  # 초기값

for i in range(2, N + 1):
    # 점화식
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[N])
