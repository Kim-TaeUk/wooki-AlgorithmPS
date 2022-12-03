arr = [5, 3, 7, 9, 2, 5, 6]
arrMin = arr[0]

for i in range(1, len(arr)):
    if arrMin > arr[i]:
        arrMin = arr[i]
print(arrMin)

arrMin = float('inf')
for x in arr:
    if arrMin > x:
        arrMin = x
print(arrMin)