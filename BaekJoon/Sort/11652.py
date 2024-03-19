import sys

N = int(sys.stdin.readline().rstrip())
cards = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
cards.sort()

cnt, max_cnt = 0, 0
max_value = float('-inf')

# i = 0일 때 index out of range 처리 빠뜨리지 않기
for i in range(N):
    if i == 0 or cards[i - 1] == cards[i]:
        cnt += 1
    else:
        if cnt > max_cnt:
            max_cnt = cnt
            max_value = cards[i - 1]
        cnt = 1

# 제일 마지막 수 처리 빠뜨리지 않기
if cnt > max_cnt:
    max_value = cards[N - 1]

print(max_value)

# 바킹독 풀이, cards를 index로 조작
