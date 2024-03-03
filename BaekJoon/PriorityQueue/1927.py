import sys


def push(data):
    global size
    size += 1
    heap.append(data)
    index = size

    while index != 1:
        parent = index // 2
        if heap[parent] <= heap[index]:
            break
        heap[parent], heap[index] = heap[index], heap[parent]
        index = parent


def top():
    return heap[1]


def pop():
    global size
    heap[1] = heap[size]
    heap.pop()
    size -= 1
    index = 1

    while 2 * index <= size:
        left_child, right_child = 2 * index, 2 * index + 1
        min_child = left_child
        if right_child <= size and heap[right_child] < heap[left_child]:
            min_child = right_child
        if heap[index] <= heap[min_child]:
            break
        heap[index], heap[min_child] = heap[min_child], heap[index]
        index = min_child


N = int(sys.stdin.readline().rstrip())
heap = [0]
size = 0
for _ in range(N):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        if size == 0:
            print(0)
        else:
            print(heap[1])
            pop()
    else:
        push(x)
