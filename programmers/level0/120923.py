def solution(num, total):
    x = ((2 * total / num) - num + 1) / 2
    return [x + i for i in range(num)]
