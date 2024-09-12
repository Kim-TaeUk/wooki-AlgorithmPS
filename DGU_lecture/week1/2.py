import random

N = int(input())
lst = random.sample(range(1, 101), N)

print("버블 정렬 시작: ")

for i in range(N):
    for j in range(N - i - 1):  # 이미 정렬된 값은 비교 X
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
    print("단계", i + 1, ":", lst)

print("최종 정렬 결과:", lst)
