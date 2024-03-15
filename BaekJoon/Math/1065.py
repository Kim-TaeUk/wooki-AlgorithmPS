import sys

X = int(sys.stdin.readline().rstrip())

if X < 100:
    print(X)
    exit()
else:
    cnt = 99
    for x in range(100, X + 1):
        a, b, c = int(str(x)[0]), int(str(x)[1]), int(str(x)[2])
        if not (a <= b <= c or a >= b >= c):
            continue
        if 2 * b == a + c:
            cnt += 1

    print(cnt)
    exit()
