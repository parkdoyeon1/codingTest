def solution(progresses, speeds):
    answer = []
    days = 0
    cnt = 0

    while len(progresses):
      # progress 와 speed, days(날짜)를 곱하여 더했을 때 100이 넘으면, 
      # 왼쪽인덱스 부터 pop을 시켜 while 문 순회 
      # 프로세스가 끝났으므로, 카운트 증가
      if progresses[0] + (speeds[0] * days) >= 100:
        progresses.pop(0)
        speeds.pop(0)
        cnt += 1
        print(cnt)
      else:
        # else 문을 거치고, 만약 카운트가 0이 넘으면 프로세스가 하나가 완료 되고, 다음 프로세스는
        # 완료되지 않았기 때문에answer에 append해준다.
        if cnt > 0:
          answer.append(cnt)
          cnt = 0
        else:
          days += 1
    # 카운트가 0이 넘으면 마지막 작업이 완료 된 것 이므로 answer에 append 해준다.
    if cnt > 0:  
        answer.append(cnt)
        
    return answer