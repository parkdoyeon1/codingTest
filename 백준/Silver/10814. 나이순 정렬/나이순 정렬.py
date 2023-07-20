import sys
user = []

setNum = int(sys.stdin.readline())

for i in range(setNum):
    age, name = sys.stdin.readline().split()
    age = int(age)
    user.append([age, name])

user.sort(key=lambda x:x[0])

# user.sort(key=lambda x:(x[0], x[1]))

for e in user:
    print(e[0], e[1])