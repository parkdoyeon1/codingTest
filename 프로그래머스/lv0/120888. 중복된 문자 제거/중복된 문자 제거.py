def solution(my_string):
    answer = ''
    i = 0
    for i in my_string:
     if i not in answer:
         answer += i
    return answer