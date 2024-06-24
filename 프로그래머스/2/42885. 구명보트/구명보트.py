from collections import deque 

def solution(people, limit):
    people.sort()
    q = deque(people)
    answer = 0

    while len(q):
      if q[0] + q[-1] <= limit:
        q.popleft()
        if len(q) != 0:
          q.pop()
        answer += 1
      else:
        q.pop()
        answer += 1
    print(answer)

    return answer