import sys

sum = 0
for _ in range(5):
    score = int(sys.stdin.readline().rstrip())
    if score < 40:
        sum += 40
    else:
        sum += score

print(sum // 5)
