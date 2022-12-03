N = int(input())
list = list(map(int, input().split()))


def digit_sum(x):  # x가 들어오면
    sum = 0
    for i in str(x):  # string으로 분리 : str(125) -> 1 2 5
        sum += int(i)  # 분리된 것을 int로 casting하여 더해주면 자릿수의 합이 됨
    return sum


max = float('-inf')
for x in list:
    sum = digit_sum(x)
    if sum > max:
        max = sum
        res = x

print(res)
