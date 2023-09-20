N = int(input())
count = [0] * 10001
for _ in range(N):
    count[int(input())] += 1

for i in range(10001):
    for _ in range(count[i]):
        print(i)

# numbers에 들어가는 수가 10,000보다 작다는 것을 활용
# 시간 초과
