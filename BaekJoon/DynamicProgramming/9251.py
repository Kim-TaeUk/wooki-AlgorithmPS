import sys

A = sys.stdin.readline().rstrip()
B = sys.stdin.readline().rstrip()
N, M = len(A), len(B)

LCS = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
for i in range(N):
    for j in range(M):
        if A[i] == B[j]:
            LCS[i + 1][j + 1] = LCS[i][j] + 1
        else:
            LCS[i + 1][j + 1] = max(LCS[i][j + 1], LCS[i + 1][j])

print(LCS[N][M])
