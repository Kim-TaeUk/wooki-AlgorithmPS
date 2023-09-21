N = int(input())
numbers = list(map(int, input().split()))

res = 0

for number in numbers:
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            res += 1

print(res)
