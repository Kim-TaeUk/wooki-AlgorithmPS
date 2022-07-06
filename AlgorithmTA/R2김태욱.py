# R - 2

n = int(input())
A = list(map(int, input().split()))
B = []

# 문제에서 주어진 조건을 그대로 옮김
for i in range(len(A)):
    for k in range(i + 1, len(A)):
        if A[i] < A[k]:
            B.append(k)
            break

print(B)
