N = int(input())

members = []
for i in range(N):
    age, name = input().split()
    members.append((int(age), name, i))

members.sort(key=lambda x: (x[0], x[2]))

for age, name, tier in members:
    print(age, name)

# age int로 형변환 안하면 틀림
# python에서 sort()는 stable하기 때문에 굳이 tier 도입 안해도 됨
