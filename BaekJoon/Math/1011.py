import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    x, y = map(int, sys.stdin.readline().split())
    distance = y - x
    sqrt = int(distance ** 0.5)
    res = 0

    if distance == sqrt * sqrt:  # 제곱수인 경우
        res = 2 * sqrt - 1
    else:  # 제곱수가 아닌 경우
        res = 2 * sqrt
        if distance > sqrt * (sqrt + 1):  # 양 옆 제곱수의 중간값을 지났는지 확인
            res += 1

    print(res)

# 관찰이 중요한 문제 - 모르겠으면 적어보자
