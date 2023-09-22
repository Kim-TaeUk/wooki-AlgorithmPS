import sys


def tobin(target):
    if target == 0:
        return
    else:
        tobin(target // 2)
        print(target % 2, end="")


Octal = list(map(int, sys.stdin.readline().rstrip()))
Decimal = 0
x = 1

for i in range(len(Octal) - 1, -1, -1):
    Decimal += x * Octal[i]
    x *= 8

tobin(Decimal)

# tobin(): O(logN)
# for loop: O(N)
# 시간복잡도 O(N)이라 괜찮을 줄 알았는데 시간 초과..
