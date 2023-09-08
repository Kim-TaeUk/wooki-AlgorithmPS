N = int(input())
body = []

for _ in range(N):
    height, weight = map(int, input().split())
    body.append((height, weight))

body.sort(reverse=True)

largest = 0
cnt = 0

for height, weight in body:
    if weight > largest:
        largest = weight
        cnt += 1

print(cnt)
