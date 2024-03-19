import sys

N = int(sys.stdin.readline().rstrip())
cards = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
cards.append(2 ** 62 + 1)  # 최대값 넣고 cards[N]까지 돌게 하는 테크닉, 마지막 카드에 대한 예외 처리 필요 없어짐
cards.sort()

cnt, max_cnt = 1, 0  # cnt 1로 놓고 cards[1]부터 돌게 하는 테크닉, i = 0일 때 예외 처리 필요 없어짐
max_value = float('-inf')

for i in range(1, N + 1):
    if cards[i - 1] == cards[i]:
        cnt += 1
    else:
        if cnt > max_cnt:
            max_cnt = cnt
            max_value = cards[i - 1]
        cnt = 1

print(max_value)

# 바킹독 개선된 풀이, cards를 index로 조작
