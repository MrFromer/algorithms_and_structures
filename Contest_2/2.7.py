import sys
from collections import deque

# Чтение количества запросов
n = int(sys.stdin.readline().strip())

# Два дека: для левой и правой части очереди
left = deque()
right = deque()

# Результат для запросов типа '-'
output = []

for _ in range(n):
    query = sys.stdin.readline().strip().split()
    if query[0] == '+':
        right.append(query[1])
    elif query[0] == '*':
        left.append(query[1])
    elif query[0] == '-':
        output.append(left.popleft() if left else right.popleft())

    # Балансировка деков
    if len(left) < len(right):
        left.append(right.popleft())
    elif len(left) > len(right) + 1:
        right.appendleft(left.pop())

# Выводим все результаты
sys.stdout.write('\n'.join(output) + '\n')
