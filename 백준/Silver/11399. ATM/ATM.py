import sys

n = int(sys.stdin.readline())

data = list(map(int, sys.stdin.readline().split()))
data.sort()
res = 0

for i in range(n+1):
    for j in range(0, i):
        res += data[j]

print(res)