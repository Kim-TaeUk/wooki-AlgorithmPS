# 3. 조건문(if 분기문, 다중 if문)
x = 14

if x == 14:
    print("Lucky")
if x != 7:
    print("Unlucky")

# 아래 3개 case가 모두 같은 의미
if x > 0:
    if x < 20:
        print("20보다 작은 자연수이다")

if x > 0 and x < 20:
    print("20보다 작은 자연수이다")

if 0 < x < 20:
    print("20보다 작은 자연수이다")

# if - else (분기)
if x > 0:
    print("양수이다")
else:
    print("음수이다")

# if - elif - else (다중 분기)
x = 93
if x >= 90:
    print('A')
elif x >= 80:
    print('B')
elif x >= 70:
    print('C')
elif x >= 60:
    print('D')
else:
    print('F')
