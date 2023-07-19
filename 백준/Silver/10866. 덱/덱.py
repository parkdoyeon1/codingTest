from collections import deque
import sys
deq = deque()
num = int(input())
y = 0
x = 0

for i in range(num):
    command = list(sys.stdin.readline().rstrip().split())

    if command[0] == "push_front":
        deq.appendleft(command[1])
    elif command[0] == "push_back":
        deq.append(command[1])

    elif command[0] == "pop_front":
        if deq:
            y = deq.popleft()
            print(y)
        else:
            print("-1")

    elif command[0] == "pop_back":
        if deq:
            print(deq.pop())
        else:
            print("-1")

    elif command[0] == "size":
        print(len(deq))

    elif command[0] == "empty":
        if deq:
            print("0")
        else:
            print("1")

    elif command[0] == "front":
        if deq:
            print(deq[0])
        else:
            print("-1")

    elif command[0] == "back":
        if deq:
            print(deq[len(deq)-1])
        else:
            print("-1")


