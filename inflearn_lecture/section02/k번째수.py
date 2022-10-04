T = int(input())

for i in range(T):
    n, s, e, k = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    print(x[k])

# 2 -> 총 두 번 반복
# 6 2 5 3 -> 6개 입력인데, 2번째 ~ 5번째 중 3번째 것
# 5 2 7 3 8 9 -> 2 3 5 7 8 9
# 2번째 ~ 5번째 : 3 5 7 8 -> 3번째 것은 7
