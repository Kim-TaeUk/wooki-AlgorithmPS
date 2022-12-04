# 10. 2차원 리스트 생성과 접근

# 1차원 list 생성
a = [0] * 10
print(a)

# 2차원 list 생성
a = [[0] * 3 for _ in range(4)]
print(a)

# list의 원소값 변경
a[0][1] = 1
print(a)
a[1][1] = 2
print(a)

# 2차원 list 출력
for x in a:  # 행 단위로
    print(x)

for x in a:  # 2중 for문으로 원소 하나하나 다 찍기
    for y in x:
        print(y, end=' ')
    print()
