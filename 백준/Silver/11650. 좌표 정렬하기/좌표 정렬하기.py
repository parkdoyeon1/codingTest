import sys

setCount = int(input())
point = []

for i in range(setCount):
    x, y = sys.stdin.readline().split()
    x = int(x)
    y = int(y)
    point.append([x, y])

point.sort(key=lambda x: (x[0], x[1]))

for e in point:
    print(e[0], e[1])