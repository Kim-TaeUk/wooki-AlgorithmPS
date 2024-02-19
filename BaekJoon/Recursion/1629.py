import sys


def func(base, exponent, modulus):
    if exponent == 1:
        return base % modulus
    tmp = func(base, exponent // 2, modulus)
    tmp = tmp * tmp % modulus
    if exponent % 2 == 0:  # 짝수면
        return tmp
    return tmp * base % modulus


A, B, C = map(int, sys.stdin.readline().split())
print(func(A, B, C))
