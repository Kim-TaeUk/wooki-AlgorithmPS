a, b = map(float, input().split())
c = a / b
print("%.3f" % c)

# print(round(c, 3))
# 이렇게 하면 10.0 / 0.0001 = 100000.000 나와야 하는데 100000.0 나와서 실패
