# 8. 리스트와 내장 함수(1)
import random as r

# list 생성 & 초기화
a = []
print(a)

a = list()
print(a)

a = [1, 2, 3, 4, 5]
print(a)
print(a[3])

b = list(range(1, 11))  # range로도 초기화 가능
print(b)

c = a + b
print(c)

# 내장 함수
# append & insert & pop & remove & index
a.append(6)
print(a)

a.insert(3, 7)  # 3번째 index에 7 삽입
print(a)

a.pop()  # 이러면 마지막 index꺼 pop
print(a)

a.pop(3)  # 3번째 index pop
print(a)

a.remove(4)  # 4를 remove
print(a)

print(a.index(5))  # a에서 5라는 값을 찾아 index를 return

# sum & max & min
a = list(range(1, 11))
print(a)
print(sum(a))  # 55
print(max(a))  # 10
print(min(a))  # 1

# shuffle <- random module에 있는 함수
r.shuffle(a)
print(a)

# sort
a.sort()  # sort 함수는 ascending order로
print(a)

a.sort(reverse=True)  # reverse = True로 주면 descending order로
print(a)

# clear
a.clear()
print(a)
