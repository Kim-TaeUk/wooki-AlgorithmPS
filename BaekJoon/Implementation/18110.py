import sys


def myround(x):
    return int(x + 0.5)


n = int(sys.stdin.readline().strip())
if n:
    score = []
    for _ in range(n):
        score.append(int(sys.stdin.readline().strip()))

    score.sort()

    cut = n * 0.15
    cut = myround(cut)

    if cut:
        score = score[cut:-cut]
    else:
        pass

    res = sum(score) / len(score)
    res = myround(res)

    print(res)
else:
    print(0)

# 어이X - 그냥 input()으로 입력받으면 시간 초과 뜸

# 파이썬 round - round_half_even 방식이므로 조심
# cut = 0일 때 고려 안하면 런타임 에러(ZeroDivisionError)
# pop, pop(0)말고 슬라이싱 하기
