# 2018112034 김태욱
def makeHeap(root, LastNode):  # heap 생성
    parent = root  # parent를 root로
    rootData = A[root]  # root의 값
    leftSon = 2 * parent + 1  # leftSon
    rightSon = leftSon + 1  # rightSon

    while leftSon <= LastNode:  # leftSon과 rightSon을 비교, 반복문으로 계속
        if rightSon <= LastNode and A[leftSon] < A[rightSon]:  # rightSon이 클 경우
            son = rightSon
        else:  # leftSon이 클 경우
            son = leftSon
        if rootData < A[son]:  # root가 son보다 크다면
            A[parent] = A[son]  # son을 위로 올림
            parent = son
            leftSon = parent * 2 + 1  # leftSon과 rightSon을 새롭게 정의
            rightSon = leftSon + 1
        else:
            break
    A[parent] = rootData


def HeapSort(n):
    i = int(n / 2)
    while i >= 0:
        makeHeap(i, n - 1)  # 정렬할 배열을 heap로 바꿈
        i -= 1
    i = n - 1
    print("make Heap : ", A)
    while i > 0:
        # heap을 생성한 이후에 최대값을 제거하고, i인덱스의 값과 교환
        A[0], A[i] = A[i], A[0]
        makeHeap(0, i - 1)  # 남은 원소들로 heap을 다시 정리
        i -= 1
    print("sort Heap : ", A)


A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
print("입력된 배열 A : ",A)
HeapSort(10)
