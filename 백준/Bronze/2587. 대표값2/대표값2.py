score = []

for i in range(5):
    score.append(int(input()))


avg = int(sum(score)/5)
print(avg)
score.sort(reverse=True)
print(score[2])