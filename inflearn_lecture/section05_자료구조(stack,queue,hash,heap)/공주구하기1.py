N, K = map(int, input().split())

prince = [x for x in range(1, N + 1)]
tmp = [x for x in range(1, N + 1)]

acc = 1
while len(tmp) != 1:
    for i in range(len(prince)):
        if prince[i] == 0:
            pass
        else:
            if acc % K == 0:
                tmp.remove(prince[i])
                prince[i] = 0
            acc += 1

print(tmp.pop())
