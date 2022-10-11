# 2018112034 김태욱
import random


def findMinimum(list, n):
    temp = list[0]  # list의 첫번째값을 일단 temp로 설정
    for i in range(1, n):  # list의 두번째값부터 반복문을 돌면서
        if list[i] < temp:  # temp와 비교하여 작다면
            temp = list[i]  # temp깂 갱신
    return temp


def findMaximum(list, n):
    temp = list[0]  # list의 첫번째값을 일단 temp로 설정
    for i in range(1, n):  # list의 두번째값부터 반복문을 돌면서
        if list[i] > temp:  # temp와 비교하여 크다면
            temp = list[i]  # temp깂 갱신
    return temp


def findMMinMax(list, n):
    if n % 2 == 1:  # 자료의 개수가 홀수일 때
        tempMax = list[0]  # list의 첫번째 값을 일단 tempMax와
        tempMin = list[0]  # tempMin으로 설정
        for i in range(1, n - 1, 2):  # list의 두번째, 세번째 이런식으로 2개씩 비교를 하는데
            if list[i] < list[i + 1]:  # 두 값을 비교하여
                small = list[i]  # 작은 값을 small에
                large = list[i + 1]  # 큰 값을 large로 설정
            else:
                small = list[i + 1]
                large = list[i]

            if small < tempMin:  # tempMin과 비교하여 작다면
                tempMin = small  # tempMin값 갱신
            if large > tempMax:  # tempMax와 비교하여 크다면
                tempMax = large  # tempMax값 갱신
        return tempMin, tempMax
    else:  # 자료의 개수가 짝수일 때
        tempMax = list[0]
        tempMin = list[0]
        for i in range(1, n - 1, 2):
            if list[i] < list[i + 1]:
                small = list[i]
                large = list[i + 1]
            else:
                small = list[i + 1]
                large = list[i]

            if small < tempMin:
                tempMin = small
            if large > tempMax:
                tempMax = large
        # 자료의 개수가 짝수일 경우는 마지막 값을 따로 한 번 비교해준다
        if list[n - 1] < tempMin:
            tempMin = list[n - 1]
        if list[n - 1] > tempMax:
            tempMax = list[n - 1]
        return tempMin, tempMax


A = random.sample(range(1, 1000001), 1000)
# 1부터 100000까지의 숫자 중 중복을 제거하고 1000개를 뽑는다

print("생성한 1000개의 random한 정수", A)
print("findMinimum으로 찾은 최소값 : ", findMinimum(A, 1000))
print("findMaximum으로 찾은 최대값 : ", findMaximum(A, 1000))
print("findMaxMin으로 찾은 최소값과 최대값 : ", findMMinMax(A, 1000))
