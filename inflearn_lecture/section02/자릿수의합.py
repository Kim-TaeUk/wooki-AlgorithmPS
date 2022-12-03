N = int(input())
list = list(map(int, input().split()))


def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x = x // 10
    return sum


max = float('-inf')
for x in list:
    sum = digit_sum(x)
    if sum > max:
        max = sum
        res = x

print(res)
