from collections import deque

essential = input()
N = int(input())
for i in range(N):
    plan = input()
    dq = deque(essential)

    for x in plan:
        if x in dq:
            if x != dq.popleft():
                print("#%d NO" % (i + 1))
                break
    else:
        if len(dq) == 0:
            print("#%d YES" % (i + 1))
        else:
            print("#%d NO" % (i + 1))

# 내가 작성한
# 풀이1 -> 쓸데없이 루프마다 조건문으로 비교한다
# 풀이2 -> 쓸데없이 plan을 다 비울 때까지 while이 돈다
# 이런 짓을 하지 않고,
# plan에서 하나씩 돌면서 dq에 있는데 dq의 첫번째와 같지 않다면(우선순위를 지키지 않았다면)
# 바로 NO를 출력해버림으로써 시간을 아낄 수 있다
