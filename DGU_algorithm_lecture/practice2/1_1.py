def iterative_bubblesort(list):  # iterative bubblesort
    for i in range(len(list)):  # 배열의 모든 원소를 순차 탐색한다
        print("정렬 중인 배열 :", A)  # 단계별로 A가 바뀌는 것을 출력
        for j in range(0, len(list) - i - 1):
            # 외부의 for문을 반복할 때마다 가장 큰 값이 맨 뒤로 가기 때문에
            # range 를 0 , len(arr) - i - 1 으로 설정
            if list[j] > list[j + 1]:  # j 번째 원소와 j + 1번째 원소를 비교하고
                list[j], list[j + 1] = list[j + 1], list[j]  # 큰 값을 뒤로 보낸다


A = [30, 20, 40, 10, 5, 1, 30, 15]

print("정렬 전의 배열 :", A)
iterative_bubblesort(A)
print("정렬 후의 배열 :", A)
