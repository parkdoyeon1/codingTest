import sys
n, m = map(int,sys.stdin.readline().split())
dbo = set()
sbo = set()
count = 0

for i in range(n):
    dbo.add(sys.stdin.readline())

for i in range(m):
    sbo.add(sys.stdin.readline())

arr = sorted(list(sbo & dbo))
print(len(arr))

for i in arr:
    print(i.strip())