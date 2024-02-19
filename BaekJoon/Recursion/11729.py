import sys


def hanoi(pillar1, pillar2, n):
    if n == 1:
        print(pillar1, pillar2)
        return
    hanoi(pillar1, 6 - pillar1 - pillar2, n - 1)  # n-1개의 원판을 기둥1 -> 기둥3
    print(pillar1, pillar2)  # n번 원판을 기둥1 -> 기둥2
    hanoi(6 - pillar1 - pillar2, pillar2, n - 1)  # n-1개의 원판을 기둥3 -> 기둥2


N = int(sys.stdin.readline().rstrip())
print((1 << N) - 1)  # 2^N -1(일반항)
hanoi(1, 3, N)
