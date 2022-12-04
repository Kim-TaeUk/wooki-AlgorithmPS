# 5. 반복문을 이용한 문제풀이
"""
1) 1부터 N까지 홀수 출력하기
2) 1부터 N까지의 합 구하기
3) N의 약수 출력하기
"""

# 문제 1
n = int(input())
for i in range(1, n + 1):  # n까지니까 n+1까지로 MAX값 주는거 인지하기
    if i % 2 == 1:
        print(i)

# 문제 2
n = int(input())
sum = 0
for i in range(1, n + 1):
    sum += i
print(sum)

# 문제 3
n = int(input())
for i in range(1, n + 1):
    if n % 1 == 0:
        print(i, end=' ')
