from collections import deque

N, M = map(int, input().split())
patient = [(idx, val) for idx, val in enumerate(list(map(int, input().split())))]
patient = deque(patient)
cnt = 0

while True:
    current = patient.popleft()

    if any(current[1] < data[1] for data in patient):
        patient.append(current)
    else:
        cnt += 1
        if current[0] == M:
            print(cnt)
            break

# any 사용하여 쉽게
# enumerat 사용하기
