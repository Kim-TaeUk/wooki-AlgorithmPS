def solution(i, j, k):
    cnt = 0
    for x in range(i, j + 1):
        for y in str(x):
            if int(y) == k:
                cnt += 1

    return cnt
