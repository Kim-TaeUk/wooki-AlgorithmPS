import sys
import math

N = int(sys.stdin.readline().rstrip())
N_factorial = str(math.factorial(N))
res = 0

if N_factorial[-1] != '0':
    print(0)
else:
    for x in reversed(N_factorial):
        if x == '0':
            res += 1
        else:
            break
    print(res)
