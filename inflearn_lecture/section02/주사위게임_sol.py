N = int(input())
res = 0
for i in range(N):
    tmp = input().split()
    tmp.sort()
    a, b, c = map(int, tmp)

    if a == b and b == c:
        money = 1000 + a * 1000
    elif a == b or a == c:  # 2가지 case 한 번에 고려
        money = 1000 + (a * 100)
    elif b == c:
        money = 1000 + (b * 100)
    else:
        money = c * 100

    if money > res:  # res 도입해서 갱신하는 방식
        res = money

print(res)
