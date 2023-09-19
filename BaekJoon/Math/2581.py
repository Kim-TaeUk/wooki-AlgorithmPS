M = int(input())
N = int(input())
prime = []

for x in range(M, N + 1):
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                break
        else:
            prime.append(x)

if len(prime) == 0:
    print(-1)
else:
    print(sum(prime))
    print(prime[0])
