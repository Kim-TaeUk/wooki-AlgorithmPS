import sys

n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    p = int(sys.stdin.readline().rstrip())
    players = []
    for _ in range(p):
        cost, name = sys.stdin.readline().split()
        players.append((int(cost), name))

    players.sort(key=lambda x: -x[0])
    print(players[0][1])
