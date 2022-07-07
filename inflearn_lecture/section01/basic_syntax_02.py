# 2. 변수입력과 연산자
a = input()
print(a)

a = input("숫자를 입력하세요 : ")
print(a)

# split
# a=2, b=3
a, b = input().split()  # white space 기준으로 분리
c = a + b
print(c)  # 출력 23
print(type(a))  # 출력 <class 'str'>
print(type(c))  # 출력 <class 'str'>

a, b = input().split()
a = int(a)
b = int(b)
print(type(a))  # 출력 <class 'int'>
print(a + b)  # 출력 5

a, b = map(int, input().split())
print(a + b)  # 출력 5
print(a / b)
print(a // b)  # 몫 연산
print(a % b)  # 나머지 연산
print(a ** b)  # 거듭 제곱

a = 4.3  # float형
b = 5  # int형
c = a + b  # float형 -> 넓은 범위로
