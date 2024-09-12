import random

N = int(input())
lst = random.sample(range(1, 101), N)

print("선택 정렬 시작: ")
for i in range(N - 1):
    min_index = i
    for j in range(i + 1, N):  # 이미 정렬된 값은 비교 X
        if lst[min_index] > lst[j]:
            min_index = j
    lst[i], lst[min_index] = lst[min_index], lst[i]
    print("단계", i + 1, ":", lst)

print("최종 정렬 결과:", lst)
