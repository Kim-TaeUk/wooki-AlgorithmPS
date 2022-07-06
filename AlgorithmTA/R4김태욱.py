# R - 4
from operator import itemgetter


def solution(food_times, k):
    foods = []  # 시간, 음식 리스트를 함께 저장할 list
    n = len(food_times)  # 음식의 총 개수
    for i in range(n):  # 반복문 이용해서 foods에 하나씩 추가
        foods.append((food_times[i], i + 1))  # 음식 먹는데 걸리는 시간, 음식번호로 저장
    foods.sort()  # 음식시간을 기준으로 정렬

    pretime = 0  # 이전 음식을 먹는데 걸리는 시간, 0으로 초기화
    for i, food in enumerate(foods):
        # 한 번에 빼주기 위해 diff 도입
        # 처음 시행 시니까 food[0] - pretime
        diff = food[0] - pretime
        if diff != 0:
            spend = diff * n  # 음식을 소비할 시간 = diff * 남은 음식의 개수
            if spend <= k:
                k -= spend
                pretime = food[0]
            else:  # spend > k 이면 한 번에 못 빼줌
                k %= n  # 남은 음식의 개수만큼 나머지 연산해서 어딘지 찾음
                # i번째 음식부터 남은 음식이니까 i:, 음식번호로 다시 정렬(itemgetter 이용)
                # 정렬된 결과를 sublist에 저장
                sublist = sorted(foods[i:], key=itemgetter(1))
                return sublist[k][1]  # 먹어야 되는 음식 번호 반환 index는 나머지 연산 결과인 k
        n -= 1  # 음식 하나를 다먹었으니까 -1, 반복마다
    return -1  # 방송 중단 전 음식을 다 먹을 때 -1 반환
