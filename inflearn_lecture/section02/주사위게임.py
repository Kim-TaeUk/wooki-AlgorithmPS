N = int(input())
prize_list = []
for i in range(N):
    a, b, c = map(int, input().split())
    # 규칙 1
    if a == b == c:
        prize = 10000 + a * 1000
    # 규칙 2
    elif a == b != c:
        prize = 1000 + a * 100
    elif b == c != a:
        prize = 1000 + b * 100
    elif c == a != b:
        prize = 1000 + c * 100
    # 규칙 3
    else:
        prize = max([a, b, c]) * 100
    prize_list.append(prize)

print(max(prize_list))
