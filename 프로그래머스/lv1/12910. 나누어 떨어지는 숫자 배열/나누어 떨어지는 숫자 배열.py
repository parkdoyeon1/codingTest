def solution(arr, divisor):
    answer = []
    j = 0
    i = 0
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    answer.sort()
    if len(answer) == 0 :
        return [-1]
    return answer   