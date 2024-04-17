lst = [1, 3, 11, 6, 7, 10, 14, 9, 18, 16, 5, 4, 2, 8, 19]
N = len(lst)  # 15

# 누적 합 배열 만들기
prefix_sum = [0 for _ in range(N + 1)]
for i in range(N):
    prefix_sum[i + 1] = prefix_sum[i] + lst[i]
# prefix_sum = [0, 1, 4, 15, 21, 28, 38, 52, 61, 79, 95, 100, 104, 106, 114, 133]

# lst[L] ~ lst[R]의 합
# = prefix_sum[R + 1] - prefix_sum[L]

print(prefix_sum[6] - prefix_sum[3])  # lst[3] ~ lst[5]의 합 = 6 + 7 + 10 = 23
