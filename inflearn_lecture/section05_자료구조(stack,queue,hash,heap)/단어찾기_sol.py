N = int(input())
poem = dict()

for _ in range(N):
    word = input()
    poem[word] = 1  # value가 다 1로

for _ in range(N - 1):
    word = input()
    poem[word] = 0

for key, value in poem.items():
    if value == 1:
        print(key)
        break

# dict 사용하기 - 아는 문법이니까
