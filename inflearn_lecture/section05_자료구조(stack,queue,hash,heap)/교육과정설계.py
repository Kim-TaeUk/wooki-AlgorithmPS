from collections import deque

essential = input()
essential = list(essential)
N = int(input())
for i in range(N):
    plan = input()
    plan = deque(plan)
    res = []

    while plan:
        current = plan.popleft()
        if current in essential and current not in res:
            res.append(current)

    if res == essential:
        print("#", i + 1, "YES")
    else:
        print("#", i + 1, "NO")
