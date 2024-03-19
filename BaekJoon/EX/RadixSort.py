# Radix Sort
# 최대 자릿수 D, 리스트 개수 K(10진수인 경우 10), 데이터 개수 N
# D번에 걸쳐 카운팅 소트를 하는 것과 같은 상황
# O(D(N + K)) -> K가 무시할 만큼 작다: O(DN)

# 최대 자릿수 구하기
def get_max_digit(lst):
    max_digit = 0
    for num in lst:
        max_digit = max(max_digit, len(str(num)))

    return max_digit


# 숫자 num의 10^a째 자릿수 구하기 (a = 1이면 10의 자리)
def get_digit_num(num, a):
    return (num // p10[a]) % 10


arr = [12, 421, 46, 674, 103, 502, 7, 100, 21, 545]
N = len(arr)
D = get_max_digit(arr)
p10 = [10 ** i for i in range(D)]  # 10의 거듭제곱 값 저장하는 list
tmp = [[] for _ in range(10)]

for i in range(D):  # 자릿수만큼 반복
    tmp = [[] for _ in range(10)]

    for j in range(N):  # 현재 자릿수에 해당하는 숫자들을 tmp에 분류
        tmp[get_digit_num(arr[j], i)].append(arr[j])

    # 각 자리수 별로 분류된 숫자들로 arr에 재할당
    arr = [x for sublist in tmp for x in sublist]

print(*arr)
