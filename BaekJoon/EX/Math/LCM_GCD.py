import math


def lcm(a, b):  # 최소공배수
    for x in range(max(a, b), (a * b) + 1):
        if x % a == 0 and x % b == 0:
            return x


def gcd(a, b):  # 최대공약수
    while b > 0:
        a, b = b, a % b
    return a


print(lcm(4, 5))  # 20
print(math.lcm(4, 5))  # 20

print(gcd(9, 36))  # 9
print(math.gcd(9, 36))  # 9
