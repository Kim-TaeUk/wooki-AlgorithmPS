import sys

A = sys.stdin.readline().rstrip()
B = sys.stdin.readline().rstrip()
C = sys.stdin.readline().rstrip()
N, M, K = len(A), len(B), len(C)

LCS = [[[0 for _ in range(K + 1)] for _ in range(M + 1)] for _ in range(N + 1)]
for i in range(N):
    for j in range(M):
        for k in range(K):
            if A[i] == B[j] == C[k]:
                LCS[i + 1][j + 1][k + 1] = LCS[i][j][k] + 1
            else:
                LCS[i + 1][j + 1][k + 1] = max(LCS[i + 1][j + 1][k], LCS[i + 1][j][k + 1], LCS[i][j + 1][k + 1])

print(LCS[N][M][K])
