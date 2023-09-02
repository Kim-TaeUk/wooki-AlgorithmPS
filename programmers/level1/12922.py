def solution(n):
    # return ('수박' * (int(n / 2) + 1))[:n]
    return '수박' * (n // 2) + '수' * (n % 2)
