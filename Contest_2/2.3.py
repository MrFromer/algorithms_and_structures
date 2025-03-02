mass = [x for x in input().split()]

stack = []

for i in range(len(mass)):
    if mass[i] == '+':
        result = int(stack[-1]) + int(stack[-2])
        stack.pop()
        stack.pop()
        stack.append(result)

    elif mass[i] == '-':
        result = int(stack[-2]) - int(stack[-1])
        stack.pop()
        stack.pop()
        stack.append(result)

    elif mass[i] == '*':
        result = int(stack[-1]) * int(stack[-2])
        stack.pop()
        stack.pop()
        stack.append(result)

    else:
        stack.append(mass[i])

print(*stack)
