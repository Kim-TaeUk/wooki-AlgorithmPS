import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

A.sort()

res = 0
for i in range(len(A)):
    res += A[i] * B.pop(B.index(max(B)))

print(res)

# A.sort(): O(NlogN)
# loop에서 B에서 max 찾기 + 제거하기: O(N) * O(N) = O(N^2)
# 총 시간복잡도: O(N^2)
