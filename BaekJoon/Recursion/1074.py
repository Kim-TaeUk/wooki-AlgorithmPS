import sys


def func(N, r, c):
    if N == 0:
        return 0
    half = 1 << (N - 1)  # 2^(N-1)

    # half보다 크거나 같은 열이나 행이 있으면 half를 빼버림으로써 보정
    if r < half and c < half:  # half보다 작은 행과 열이라면 결국 이전 단계와 결과가 같음
        return func(N - 1, r, c)
    if r < half and c >= half:
        return half * half + func(N - 1, r, c - half)
    if r >= half and c < half:
        return 2 * half * half + func(N - 1, r - half, c)
    if r >= half and c >= half:
        return 3 * half * half + func(N - 1, r - half, c - half)


N, r, c = map(int, sys.stdin.readline().split())
print(func(N, r, c))
