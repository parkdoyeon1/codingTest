n = int(input())

for i in range(n):
    stack = []
    str = input()
    for j in str:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if len(stack) == 0:
                print('NO')
                break
            else:
                stack.pop()
    else:
        if len(stack) == 0:
            print('YES')
        else:
            print('NO')