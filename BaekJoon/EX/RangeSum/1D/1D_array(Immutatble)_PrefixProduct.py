lst = [1, 2, 3, 2, 3, 2, 1, 5, 4, 2, 3, 1, 5, 2, 4]
N = len(lst)  # 15

# 누적 곱 배열 만들기
prefix_product = [1 for _ in range(N + 1)]
for i in range(N):
    prefix_product[i + 1] = prefix_product[i] * lst[i]
# prefix_product = [1, 1, 2, 6, 12, 36, 72, 72, 360, 1440, 2880, 8640, 8640, 43200, 86400, 345600]


# lst[L] ~ lst[R]의 곱
# = prefix_product[R + 1] / prefix_product[L]

print(prefix_product[6] / prefix_product[3])  # lst[3] ~ lst[5]의 곱 = 2 * 3 * 2 = 12
