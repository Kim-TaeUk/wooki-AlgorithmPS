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

# prize_list 도입하지 말고 res 변수 하나 두고 money와 비교해서 갱신하는 식으로 해도 될 듯(해설처럼)
