# P - 2
n = int(input())
dp = [0] * 30001

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1  # 현재의 수에서 1을 빼는 경우

    if i % 5 == 0:  # 현재 수가 5의 배수일 때
        dp[i] = min(dp[i], dp[i // 5] + 1)
    elif i % 3 == 0:  # 현재 수가 3의 배수일 때
        dp[i] = min(dp[i], dp[i // 3] + 1)
    elif i % 2 == 0:  # 현재 수가 2의 배수일 때
        dp[i] = min(dp[i], dp[i // 2] + 1)

print(dp[n])
