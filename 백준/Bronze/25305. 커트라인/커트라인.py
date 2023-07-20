a, b = map(int, input().split())
res = list(map(int, input().split()))


res.sort(reverse=True)
print(res[b-1])