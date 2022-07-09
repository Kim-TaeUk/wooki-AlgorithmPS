# 2. 변수 입력과 연산자
a = input()  # 출력문 X
print(a)

a = input("숫자를 입력하세요 : ")  # 출력문 O
print(a)

b = input()  # input()은 default가 string
b = int(input())  # int로 casting

# split
# a=2, b=3
a, b = input().split()  # white space 기준으로 분리
c = a + b  # string이라 concatenation
print(c)  # 출력 23
print(type(a))  # 출력 <class 'str'>
print(type(c))  # 출력 <class 'str'>

a = 'Hello World!'
print(a.split())  # print도 split() 가능 -> 출력 : ['Hello', 'World!']

a, b = input().split()
a = int(a)
b = int(b)
print(type(a))  # 출력 <class 'int'>
print(a + b)  # 출력 5

str_list = ['1', '2']  # 문자 1과 문자 2로 이루어진 str_list
a, b = map(int, str_list)  # map이용해서 a, b 각각을 int형 1, 2로 변환
print(type(a), type(b))  # int형 나오고
print(a, b)  # 숫자 1 숫자 2 나옴

a, b = map(int, input().split())  # list로 int형으로 casting된 값을 입력 받기
print(a + b)  # 출력 5
print(a / b)
print(a // b)  # 몫 연산
print(a % b)  # 나머지 연산
print(a ** b)  # 거듭 제곱

a = 4.3  # float형
b = 5  # int형
c = a + b  # float형 -> 넓은 범위로
