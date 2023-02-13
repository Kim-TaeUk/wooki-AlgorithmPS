def solution(msg):
    msg = msg.lower()
    cnt_p = msg.count('p')
    cnt_y = msg.count('y')
    print(cnt_y)
    print(cnt_p)

    if cnt_y == cnt_p:
        return True
    else:
        return False
