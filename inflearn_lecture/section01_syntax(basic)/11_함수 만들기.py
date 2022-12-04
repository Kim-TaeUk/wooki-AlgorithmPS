# 11. 함수 만들기
def add1(a, b):
    c = a + b
    print(c)


add1(3, 2)


def add2(a, b):
    c = a + b
    return c


print(add2(3, 2))

x = add2(3, 2)
print(x)


def add3(a, b):
    c = a + b
    d = a - b
    return c, d  # 값 2개도 return 가능 -> tuple로 반환


print(add3(3, 2))


def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


a = [12, 13, 7, 9, 19]
for x in a:
    if isPrime(x):
        print(x, end=' ')
