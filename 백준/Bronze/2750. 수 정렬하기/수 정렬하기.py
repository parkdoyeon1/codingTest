n = int(input())
res = []

for i in range(n):
    res.append(int(input()))


res = sorted(res)

for i in range (len(res)):
    print(res[i])