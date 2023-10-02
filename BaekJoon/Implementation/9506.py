import sys

while True:
    n = int(sys.stdin.readline().rstrip())
    if n == -1:
        break
    divisor = [1]

    for i in range(2, n):
        if n % i == 0:
            divisor.append(i)

    if n == sum(divisor):
        print(n, "=", end=" ")
        for i in range(len(divisor)):
            if i == len(divisor) - 1:
                print(divisor[i])
            else:
                print(divisor[i], end=" + ")
    else:
        print(n, "is NOT perfect.")
