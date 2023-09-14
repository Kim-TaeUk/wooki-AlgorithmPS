N = int(input())
scores = list(map(int, input().split()))

largest = max(scores)
sum = 0
for score in scores:
    sum += score * 100 / largest

avg = sum / N
print(avg)
