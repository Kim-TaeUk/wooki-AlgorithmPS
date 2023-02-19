def solution(arr, divisor):
    answer = []

    if divisor == 1:
        arr.sort()
        return arr
    else:
        for i in range(len(arr)):
            if arr[i] % divisor == 0:
                answer.append(arr[i])
        answer.sort()

        if len(answer) == 0:
            return [-1]
        else:
            return answer
