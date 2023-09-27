import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

A.sort()
B.sort(reverse=True)

res = 0
for i in range(len(A)):
    res += A[i] * B[i]

print(res)

# A.sort(), B.sort(): O(NlogN)
# loop에서 요소 하나씩 처리: O(N)
# 총 시간복잡도: O(NlogN)
