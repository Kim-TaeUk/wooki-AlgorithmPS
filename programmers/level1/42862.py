def solution(n, lost, reserve):
    lst = [1 for _ in range(n)]
    for idx in lost:
        lst[idx - 1] -= 1
    for idx in reserve:
        lst[idx - 1] += 1
    lst = [3] + lst + [3]

    for i in range(1, n + 1):
        if lst[i] == 2:
            if lst[i - 1] == 0 and lst[i + 1] == 0:
                continue
            elif lst[i - 1] == 0:
                lst[i] -= 1
                lst[i - 1] += 1
            elif lst[i + 1] == 0:
                lst[i] -= 1
                lst[i + 1] += 1

    for i in range(1, n):
        if lst[i] == 2:
            if lst[i - 1] == 0:
                lst[i] -= 1
                lst[i - 1] += 1
            elif lst[i + 1] == 0:
                lst[i] -= 1
                lst[i - 1] += 1

    return sum(1 for x in lst if x == 1 or x == 2)
