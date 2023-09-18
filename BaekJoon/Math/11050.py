import math

N, K = map(int, input().split())

# 1. math 라이브러리 이용
print(math.factorial(N) // (math.factorial(K) * math.factorial(N - K)))


# 2. 재귀 구현
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# 3. 반복문 구현
# def factorial(n):
#     if n == 0:
#         return 1
#     res = 1
#     for i in range(1, n + 1):
#         res *= i
#     return res
