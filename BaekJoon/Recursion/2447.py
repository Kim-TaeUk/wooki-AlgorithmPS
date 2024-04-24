import sys


def draw(i, j, N):
    if (i // N) % 3 == 1 and (j // N) % 3 == 1:
        print(' ', end='')
    else:
        if N // 3 == 0:
            print('*', end='')
        else:
            draw(i, j, N // 3)


N = int(sys.stdin.readline().rstrip())
for i in range(N):
    for j in range(N):
        draw(i, j, N)
    print('')
# Pypy3로 AC
