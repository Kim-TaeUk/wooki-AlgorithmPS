import sys

N = int(sys.stdin.readline().rstrip())
scores = [0]
for _ in range(N):
    scores.append(int(sys.stdin.readline().rstrip()))

if N == 1:  # N = 1 예외처리 안해주면 for 문에서 에러 발생
    print(scores[1])
    exit()

dp = [[0 for _ in range(3)] for _ in range(N + 3)]
# 초기값
dp[1][1] = scores[1]
dp[1][2] = 0
dp[2][1] = scores[2]
dp[2][2] = scores[1] + scores[2]

for i in range(3, N + 1):
    # 점화식
    # dp[i][j]: 현재까지 j개의 계단을 연속해서 밟고 i번째 계단까지 올라섰을 때 점수의 최댓값
    # (단, i번째 계단은 반드시 밟아야 함)
    # -> 2차원이여야만 지금까지 몇개의 계단을 밟았는지에 대한 정보를 알 수 있음
    dp[i][1] = max(dp[i - 2][1], dp[i - 2][2]) + scores[i]
    dp[i][2] = dp[i - 1][1] + scores[i]

print(max(dp[N][1], dp[N][2]))
