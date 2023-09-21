import sys

N = int(sys.stdin.readline().strip())
count = [0] * 10001
for _ in range(N):
    count[int(sys.stdin.readline().strip())] += 1

for i in range(10001):
    for _ in range(count[i]):
        print(i)

# numbers에 들어가는 수가 10,000보다 작다는 것을 활용
# 시간 초과 -> sys로 해결
