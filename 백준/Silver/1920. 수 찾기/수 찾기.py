import sys

set_count1 = int(sys.stdin.readline())


data1 = list(map(int, sys.stdin.readline().split()))

set_count2 = int(sys.stdin.readline())

data2 = list(map(int, sys.stdin.readline().split()))
s = set(data1).intersection(data2)

for e in data2:
    if e in s:
        print(1)
    else:
        print(0)

        