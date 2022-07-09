# 9. 리스트와 내장 함수(2)
a = [23, 12, 36, 53, 19]

print(a[:3])  # index ~ 2까지 출력
print(a[1:4])  # index 1 ~ 3까지 출력
print(len(a))

for i in range(len(a)):
    print(a[i], end=' ')
print()

for i in a:
    print(i, end=' ')
print()

# enumerate
for i in enumerate(a):  # tuple로 (index, value)
    print(i, end=' ')
print()

"""
# tuple & list
tuple의 값은 assignment 불가능
list의 값은 assignment 가능
나머지는 동일
"""
for i in enumerate(a):
    print(i[0], i[1])  # tuple값으로 print해주기
print()

# 가장 많이 사용하는 방식
for index, value in enumerate(a):
    print(index, value)
print()

# all & any
if all(60 > x for x in a):
    print("YES")
else:
    print("NO")

if any(11 > x for x in a):
    print("YES")
else:
    print("NO")
