def push(data):
    global size  # date를 push 해야하기 때문에 size 전역 변수로 선언
    size += 1  # 크기 1 증가시키고
    heap[size] = data  # heap에 새로운 데이터 data를 넣어줌
    index = size  # 새로 삽입한 data의 인덱스를 index에 저장

    while index != 1:  # 루트 노드까지 반복
        parent = index // 2  # 부모 노드의 인덱스 만들고
        if heap[parent] <= heap[index]:  # 최소 힙 조건 확인
            break
        # 부모노드 값이 더 크니까 swap
        heap[parent], heap[index] = heap[index], heap[parent]
        index = parent  # 새로운 데이터가 부모 노드로 이동했으니까 인덱스 update


def top():
    return heap[1]  # 가장 작은 값 반환 = 루트 노드 반환


def pop():
    global size
    # 루트에 있는 값을 마지막 노드의 값으로 교체, 크기 1 감소 시키기 -> pop 수행
    heap[1] = heap[size]
    size -= 1
    index = 1  # 인덱스도 1로 설정해주기 (루트 노드부터 시작해서 최소 힙 조건 맞게 만들어주려고)

    # index의 2배가 size보다 크면 leaf 노드라는 의미 -> leaf 노드일 때는 최소 힙 조건을 맞춰줄 필요가 없음
    while 2 * index <= size:
        left_child, right_child = 2 * index, 2 * index + 1  # 왼쪽, 오른쪽 자식 인덱스 설정하고
        min_child = left_child  # 왼쪽 자식을 먼저 최소값으로 설정 (temp) -> 오른쪽 자식은 없을 수도 있음
        # 오른쪽 자식이 존재하고, 오른쪽 자식이 왼쪽 자식보다 작다면 오른쪽 자식으로 최소값 update
        if right_child <= size and heap[right_child] < heap[left_child]:
            min_child = right_child
        # 현재 노드의 값이 (자식들의)최소 값보다 작다면 최소 힙 조건을 만족하니 break
        if heap[index] <= heap[min_child]:
            break
        # 부모 노드의 값이 더 크니까 swap
        heap[index], heap[min_child] = heap[min_child], heap[index]
        index = min_child  # 맞춰가고자 하는 데이터가 이동했으니까 인덱스 update


heap = [0] * 100005
size = 0  # heap에 들어있는 원소의 수
