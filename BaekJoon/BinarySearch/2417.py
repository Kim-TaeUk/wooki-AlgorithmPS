n = int(input())

left = 1
right = n
res = 0

while left <= right:
    mid = (left + right) // 2

    if mid * mid <= n:
        res = mid
        left = mid + 1
    elif mid * mid > n:
        right = mid - 1

# if n % res == 0:
# 이렇게 하면 틀림
# 반례 input 9223372030926249000, output 3037000498, answer 3037000499
# 3,037,000,498 ^ 2 = 9,223,372,024,852,248,004로 9,223,372,030,926,249,000가 아니지만,
# 9,223,372,030,926,249,000 % 3,037,000,498 = 0이 출력됨. -> 부동 소수점 오차로 인해 정확한 결과가 아님
if res * res == n:
    print(res)
else:
    print(res + 1)

print(9223372030926249000 % 3037000498)
