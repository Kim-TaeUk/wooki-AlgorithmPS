import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    coins = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline().rstrip())

    dp = [0 for _ in range(M + 1)]
    dp[0] = 1
    for i in range(N):
        coin = coins[i]
        for j in range(coin, M + 1):
            dp[j] += dp[j - coin]
    print(dp[M])
