import sys

N, M = map(int, sys.stdin.readline().split())

board = []
res = []
for _ in range(N):
    board.append(sys.stdin.readline())

for startXidx in range(N - 7):
    for startYidx in range(M - 7):
        cnt1 = 0
        cnt2 = 0

        for x in range(startXidx, startXidx + 8):
            for y in range(startYidx, startYidx + 8):
                if (x + y) % 2 == 0:
                    if board[x][y] != 'W':
                        cnt1 += 1
                    if board[x][y] != 'B':
                        cnt2 += 1
                else:
                    if board[x][y] != 'B':
                        cnt1 += 1
                    if board[x][y] != 'W':
                        cnt2 += 1

        res.append(min(cnt1, cnt2))

print(min(res))

# x, y index의 짝수면 다 같은 색, 홀수면 다 같은 색이라는 규칙을 찾기 어려웠음
# bruteforce 생각이 들긴 했지만, 4중 for문에서 좀 멈칫함
