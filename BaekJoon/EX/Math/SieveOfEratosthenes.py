N = 1000  # N까지
lst = [True for _ in range(N + 1)]
lst[0], lst[1] = False, False

for i in range(2, int(N ** 0.5) + 1):
    if lst[i]:
        j = 2
        while i * j <= N:
            lst[i * j] = False
            j += 1

for i in range(N + 1):
    if lst[i]:
        print(i, end=" ")
