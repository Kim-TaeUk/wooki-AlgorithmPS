S = int(input())

sum = 0
x = 0
while True:
    sum += x
    if sum > S:
        print(x - 1)
        break

    x += 1
