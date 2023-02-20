def solution(left, right):
    res = 0
    for i in range(left, right + 1):
        if i ** (1 / 2) == int(i ** (1 / 2)):
            res -= i
        else:
            res += i

    return res
