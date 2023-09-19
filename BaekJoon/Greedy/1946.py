import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    N = int(sys.stdin.readline().strip())
    scores = []
    for _ in range(N):
        resume, interview = map(int, sys.stdin.readline().split())
        scores.append((resume, interview))

    scores.sort()

    highest = float('inf')
    cnt = 0
    for resume, interview in scores:
        if interview < highest:
            highest = interview
            cnt += 1

    print(cnt)

# sys 안쓰고 input()으로 입력받으면 시간 초과 뜸
