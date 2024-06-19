n = int(input())

ls = []
for i in range(n):
    ls.append(list(map(int, input().split())))

ls.sort(key=lambda x: (x[1], x[0]))

meetings = ls[0]
answer = 1

for i in range(1, n):
    if meetings[1] <= ls[i][0]:
        meetings = ls[i]
        answer += 1

print(answer)