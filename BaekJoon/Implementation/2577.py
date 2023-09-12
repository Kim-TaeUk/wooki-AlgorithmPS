A = int(input())
B = int(input())
C = int(input())

res = list(str(A * B * C))
numbers = "0123456789"

for number in numbers:
    print(res.count(number))
