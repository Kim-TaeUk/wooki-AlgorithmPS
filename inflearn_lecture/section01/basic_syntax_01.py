# 1. 변수와 출력함수
"""
변수명 정하기
1) 영문은 숫자와 _로 이루어진다
2) 대소문자를 구분한다
3) 문자나 _로 시작한다
4) 특수문자를 사용하면 안된다
5) 키워드를 사용하면 안된다
"""

a = 1
A = 2
A1 = 3
_b = 4
# 2b=4 -> error 발생
print(a, A, A1, _b)  # 1 2 3 4

x, y, z = 3, 2, 1
print(x, y, z)  # 3 2 1

# 값 swap
a, b = 10, 20
print(a, b)  # 10 20
a, b = b, a
print(b, a)  # 20 10

# 변수 타입
a = 12345
print(type(a))  # <class 'int'>

a = 12.123
print(a)  # 8byte까지만 출력됨 # 12.123
print(type(a))  # <class 'float'>

a = 'student'
print(a)  # student
a = "student"
print(a)  # student
print(type(a))  # <class 'str'>

# 출력 방식
print("number")  # number

a, b, c = 1, 2, 3
print(a, b, c)  # 1 2 3

print("number : ", a, b, c)  # number :  1 2 3

# sep와 end
print(a, b, c, sep='')  # 123
print(a, b, c, sep=',')  # 1,2,3

# 동일한 출력(1,2)
# 출력 1
print(a, b, c, sep='\n')

# 출력 2
print(a)
print(b)
print(c)

# 동일한 출력(1,2,3)
# 출력 1
print(a, b, c)

# 출력 2
print(a, b, c, sep=' ')

# 출력 3
print(a, end=' ')
print(b, end=' ')
print(c, end=' ')
