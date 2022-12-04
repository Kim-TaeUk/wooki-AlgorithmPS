N = int(input())
list = list(map(int, input().split()))

sum = 0  # 점수의 합
weight = 0  # 가중치
for x in list:
    if x == 1:
        weight += 1
        sum += weight
    else:
        weight = 0

print(sum)

# 내 풀이처럼 굳이 list에 넣지 않아도 할 수 있음
