arr = list(map(int, input()))
result = 0

for i in range(len(arr)):
    if result < 2 or arr[i] < 2:
        result += arr[i]
    else:
        result *= arr[i]

print(result)
