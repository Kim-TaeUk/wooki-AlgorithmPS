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
print(a, A, A1, _b)

x, y, z = 3, 2, 1
print(x, y, z)

# 값 swap
a, b = 10, 20
print(a, b)
a, b = b, a
print(b, a)

# 변수 타입
a = 12345
print(type(a))

a = 12.123
print(a)  # 8byte까지만 출력됨
print(type(a))

a = 'student'
print(a)
a = "student"
print(a)
print(type(a))

# 출력 방식
print("number")

a, b, c = 1, 2, 3
print(a, b, c)

print("number : ", a, b, c)

# sep와 end
print(a, b, c, sep='')
print(a, b, c, sep=',')

print(a, b, c, sep='\n')  # 아래 3줄과 동일
print(a)
print(b)
print(c)

print(a, b, c, sep=' ')  # 아래 3줄과 동일
print(a, end=' ')
print(b, end=' ')
print(c, end=' ')
