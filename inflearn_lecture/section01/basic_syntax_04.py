# 4. 반복문(for, while, break, continue)

"""
argument가 1개일 때 : range(MAX) -> 0 <= x < MAX
argument가 2개일 때 : range(MIN, MAX) -> MIN <= x < MAX
argument가 3개일 때 : range(MIN, MAX, GAP)
"""

# range
a = range(10)  # range -> 0 부터 9까지 list를 생성
print(list(a))

a = range(1, 10)  # 1 부터 9까지 list 생성

# for
for i in range(10):  # 0 부터 9까지 10바퀴를 돈다
    print("hello")
    print(i)

for i in range(1, 11):  # 1부터 +1 10까지
    print(i)

for i in range(10, 0, -2):  # 10부터 2까지 -2되면서
    print(i)

# while
i = 1
while i <= 10:
    print(i)
    i = i + 1  # i += 1

i = 10
while i >= 1:
    print(i)
    i = i - 2

# break
i = 1
while True:
    print(i)
    if i == 20:
        break
    i += 1

# continue : if
for i in range(1, 11):
    if i % 2 == 0:  # 짝수는 제외
        continue
    print(i)

# continue : for - else
for i in range(1, 11):
    print(i)
    if i > 12:
        break
else:  # break되면 else를 실행 X
    print(100)
