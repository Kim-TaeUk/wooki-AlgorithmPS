N = int(input())

for i in range(N):
    msg = input()
    msg = msg.upper()  # 대소문자 구문 안하니까 대문자로 처리

    for j in range(len(msg) // 2):  # 절반까지만 비교
        if msg[j] != msg[-j - 1]:
            print("#", i + 1, "NO")
            break
    else:
        print("#", i + 1, "YES")
