import sys

T = int(sys.stdin.readline().rstrip())

# dp[i] = i를 1, 2, 3의 합으로 나타내는 방법의 수
dp = [0 for _ in range(20)]
dp[1], dp[2], dp[3] = 1, 2, 4  # 초기값

for i in range(4, 12):
    # 점화식
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    print(dp[N])
