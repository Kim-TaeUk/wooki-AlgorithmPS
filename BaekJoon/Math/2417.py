import math

n = int(input())

tmp = int(math.sqrt(n))

if tmp * tmp < n:
    tmp += 1
print(tmp)

# 이분 탐색 대신 math 라이브러리 사용 - 제곱근 자체를 이용한 풀이
