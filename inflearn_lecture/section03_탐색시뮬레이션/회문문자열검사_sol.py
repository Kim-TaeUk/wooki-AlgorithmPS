N = int(input())

for i in range(N):
    msg = input()
    msg = msg.upper()

    if msg == msg[::-1]:
        print("#", i + 1, "YES")
    else:
        print("#", i + 1, "NO")

# 이런 식으로 구현하면 내 풀이처럼 직접 비교해보라고 할 수 있다
# 파이썬스럽긴 하지만 지양해야 하는 풀이

# # 문자열 거꾸로 출력 방법 4가지
# msg = "abcde"

# # 방법 1 - for문 이용
# # 빈 문자열(msg_reverse) 이용하여 기존 문자열에서 차례대로 가져오기
# msg_reverse = ''
# for x in msg:
#     msg_reverse = x + msg_reverse
# print(msg_reverse)

# # 방법 2 - reverse() 이용
# # reverse() -> list에만 사용 가능
# # reverse() 사용하기 위해서 문자열 -> list, reverse된 list를 join하여 다시 문자열로
# msg_list = list(msg)
# msg_list.reverse()
# print("".join(msg_list))

# # 방법 3 - reversed() 이용
# # reversed() 이용
# # reversed()는 문자열에 바로 적용 가능
# print("".join(reversed(msg)))

# # 방법 4 - index 처리
# print(msg[::-1])

# # index 처리 추가 설명
# print(msg[::-2])  # eca출력됨
