import sys


def check(word):
    tmp = word[0]
    check_list = [tmp]
    for x in word:
        if x == tmp:
            continue
        elif x != tmp:
            if x in check_list:
                return 0
            else:
                tmp = x
                check_list.append(tmp)
    return 1


N = int(sys.stdin.readline().rstrip())
res = 0
for _ in range(N):
    word = sys.stdin.readline().rstrip()
    res += check(word)
print(res)
