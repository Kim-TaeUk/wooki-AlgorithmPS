N = int(input())
list = list(map(int, input().split()))

# avg = round(sum(list) / len(list))  # 평균 구하고 첫째 자리에서 반올림
# 파이썬에서 round는 round_half_even 방식이므로 아래처럼 해야한다.
avg = sum(list) / len(list)
avg += 0.5
avg = int(avg)
print(avg)

# 편차의 절대값 구함
deviation = []
for i in list:
    deviation.append(abs(i - avg))

# 평균과 원소값 차이의 최소를 구함
x_min = deviation[0]
for i in deviation:
    if x_min >= i:
        x_min = i

# 편차가 최소인 인덱스를 저장
minimum_deviation_index = []
for i in range(len(deviation)):
    if deviation[i] == x_min:
        minimum_deviation_index.append(i)

# 편차가 최소인 인덱스의 list값 중 최대값들의 인덱스만 y에 저장
y = []
ans_number = list[minimum_deviation_index[0]]
for i in range(1, len(minimum_deviation_index)):
    if ans_number <= list[minimum_deviation_index[i]]:
        ans_number = list[minimum_deviation_index[i]]
        y.append(minimum_deviation_index[i])

print(avg, y[0] + 1)  # y의 첫번째 값(=평균과 가까운 점수 중 가장 높은 점수 중 학생번호가 빠른 번호 -1)
