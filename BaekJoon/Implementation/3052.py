numbers = []
for _ in range(10):
    numbers.append(int(input()))

res = set()

for x in numbers:
    res.add(x % 42)

print(len(res))
