N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(input()))

numbers.sort()
for number in numbers:
    print(number)

# 메모리 초과
# 1 ≤ N ≤ 10,000,000, 메모리 제한 8MB라서 적절하지 않은 방법임
