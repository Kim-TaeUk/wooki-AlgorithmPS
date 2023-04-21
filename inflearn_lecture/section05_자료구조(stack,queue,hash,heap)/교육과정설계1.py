from collections import deque

essential = input()
essential = list(essential)
N = int(input())
for i in range(N):
    plan = input()
    plan = deque(plan)
    res = []

    while True:
        current = plan.popleft()
        if current in essential and current not in res:
            res.append(current)

        if res == essential:
            print("#", i + 1, "YES")
            break
        else:
            if len(plan) == 0:
                print("#", i + 1, "NO")
                break

# plan과 essential이 같은지 루프마다 조건문으로 비교하는 코드
