numbers = list(map(int, input().split()))

sum = 0
for x in numbers:
    sum += x ** 2

print(sum % 10)
