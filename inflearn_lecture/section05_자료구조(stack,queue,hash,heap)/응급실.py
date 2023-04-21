from collections import deque

N, M = map(int, input().split())
patient = list(map(int, input().split()))

patient = deque(patient)
idx = deque([x for x in range(N)])
target = patient[M]
targetIdx = M
cnt = 0

while True:
    if max(patient) == patient[0]:
        cnt += 1
        if target == patient[0] and targetIdx == idx[0]:
            print(cnt)
            break
        patient.popleft()
        idx.popleft()
    else:
        patient.append(patient.popleft())
        idx.append(idx.popleft())
