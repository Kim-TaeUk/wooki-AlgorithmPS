N = int(input())

for _ in range(N):
    TC = input()

    res = 0
    score = 0

    for i in range(len(TC)):
        if TC[i] == 'X':
            score = 0
        elif TC[i] == 'O':
            score += 1
            res += score

    print(res)
