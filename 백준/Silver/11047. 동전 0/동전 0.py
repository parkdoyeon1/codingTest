import sys
import math

n, k = map(int, sys.stdin.readline().split())
cent = []
count = 0

for i in range(n):
    cent.append(int(sys.stdin.readline()))
cent.sort(reverse=True)

for i in cent:
    count += k//i
    k = k % i

print(count)