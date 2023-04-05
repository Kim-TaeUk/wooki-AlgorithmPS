msg = input()
res = 0

for x in msg:
    if x.isdecimal():
        res = res * 10 + int(x)
print(res)

cnt = 0
for i in range(1, res + 1):
    if res % i == 0:
        cnt += 1

print(cnt)

# 숫자들 붙여서 자릿수 곱해주는 아이디어 사용 좀 할 것.. -> 6번째 line
