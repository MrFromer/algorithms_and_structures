import sys

# Чтение количества событий
n = int(sys.stdin.readline().strip())

# Очередь для обработки событий
from collections import deque
queue = deque()

# Множество для быстрого поиска позиции человека в очереди
positions = {}

# Вывод для событий типа 4 и 5
output = []

for _ in range(n):
    event = sys.stdin.readline().strip().split()
    event_type = int(event[0])

    if event_type == 1:  # новый человек с уникальным номером id
        id = int(event[1])
        queue.append(id)
        positions[id] = len(queue) - 1

    elif event_type == 2:  # человек спереди уходит
        if queue:
            left = queue.popleft()
            del positions[left]
            # обновляем позиции
            for i, person in enumerate(queue):
                positions[person] = i

    elif event_type == 3:  # последний человек уходит
        if queue:
            last = queue.pop()
            del positions[last]

    elif event_type == 4:  # сколько людей перед человеком с id = q
        q = int(event[1])
        if q in positions:
            output.append(str(positions[q]))
        else:
            output.append("-1")

    elif event_type == 5:  # кто стоит первым
        if queue:
            output.append(str(queue[0]))
        else:
            output.append("-1")

# Выводим все результаты
print("\n".join(output))
