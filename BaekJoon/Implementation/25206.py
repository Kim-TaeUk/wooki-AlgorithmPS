import sys

sum_credit = 0
sum_grade = 0
for _ in range(20):
    name, credit, grade = map(str, sys.stdin.readline().split())
    if grade == 'P':
        continue
    sum_credit += float(credit)
    if grade == 'A+':
        sum_grade += 4.5 * float(credit)
    elif grade == 'A0':
        sum_grade += 4.0 * float(credit)
    elif grade == 'B+':
        sum_grade += 3.5 * float(credit)
    elif grade == 'B0':
        sum_grade += 3.0 * float(credit)
    elif grade == 'C+':
        sum_grade += 2.5 * float(credit)
    elif grade == 'C0':
        sum_grade += 2.0 * float(credit)
    elif grade == 'D+':
        sum_grade += 1.5 * float(credit)
    elif grade == 'D0':
        sum_grade += 1.0 * float(credit)
    elif grade == 'F':
        sum_grade += 0

print(sum_grade / sum_credit)
