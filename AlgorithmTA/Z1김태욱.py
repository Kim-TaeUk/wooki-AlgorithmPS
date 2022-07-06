num = int(input())
list = []

for i in range(num):
    list.append(int(input()))

answer = max(list) - min(list)
print(answer)

# list에서 최대 최소 찾는 함수 존재함, min / max
