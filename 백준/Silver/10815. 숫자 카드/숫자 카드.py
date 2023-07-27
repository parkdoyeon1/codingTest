import sys
n = int(sys.stdin.readline())
card = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
guessCard = list(map(int, sys.stdin.readline().split()))

for i in guessCard:
    if i in card:
        print(1, end= " ")
    else:
        print(0, end= " ")