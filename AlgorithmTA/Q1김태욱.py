# Q - 1
arr = list(map(int, input().split()))

# 일단 다 0으로 초기화
asc_cnt = 0
desc_cnt = 0
asc_tmp = 0
desc_tmp = 0

for i in range(len(arr) - 1):  # 반복문 이용해서
    if arr[i] < arr[i + 1]:  # i번째 원소 < i+1번째 원소면
        asc_tmp += 1  # asc_tmp을 +1
        desc_tmp = 0
    elif arr[i] > arr[i + 1]:  # i번째 원소 > i+1번째 원소면
        desc_tmp += 1  # desc_tmp을 +1
        asc_tmp = 0

    if asc_cnt < asc_tmp:
        asc_cnt = asc_tmp
    if desc_cnt < desc_tmp:
        desc_cnt = desc_tmp

if asc_cnt == 0:
    print(1, end=" ")
else:
    print(asc_cnt, end=" ")
if desc_cnt == 0:
    print(1)
else:
    print(desc_cnt)
