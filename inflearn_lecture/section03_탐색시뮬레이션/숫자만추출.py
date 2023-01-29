msg = input()
num_list = []

for x in msg:
    if x.isdigit():  # isdigit()으로 숫자만
        num_list.append(x)  # num_list에 append

num_list = "".join(num_list)  # 문자열로 만들고
num = int(num_list)  # int로 casting

cnt = 0
for i in range(1, num + 1):
    if num % i == 0:
        cnt += 1

print(num)
print(cnt)
