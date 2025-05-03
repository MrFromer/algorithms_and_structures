from sys import stdin
from sortedcontainers import SortedDict

input = stdin.readline

n = int(input())

# Словарь: ключ — левая граница, значение — (правая, цвет)
segments = SortedDict()
black_count = 0
black_total = 0

def split(x):
    """Разделить отрезок в точке x, если нужно"""
    if x in segments:
        return
    i = segments.bisect_right(x)
    if i == 0:
        return
    l = segments.iloc[i - 1]
    r, color = segments[l]
    if x < r:
        # Разбиваем [l, r) на [l, x) и [x, r)
        segments.pop(l)
        segments[l] = (x, color)
        segments[x] = (r, color)

        if color == 'B':
            global black_total, black_count
            black_total -= (r - l)
            black_total += (x - l) + (r - x)
            black_count += 1  # один отрезок стал двумя

for _ in range(n):
    c, x, l = input().split()
    x = int(x)
    l = int(l)
    y = x + l

    # Разбить по x и y
    split(x)
    split(y)

    # Удалим все между x и y
    to_delete = []
    i = segments.bisect_left(x)
    while i < len(segments):
        lkey = segments.iloc[i]
        rkey, color = segments[lkey]
        if lkey >= y:
            break
        to_delete.append(lkey)
        i += 1

    for key in to_delete:
        rkey, color = segments.pop(key)
        if color == 'B':
            black_total -= (rkey - key)
            black_count -= 1

    if c == 'B':
        # Добавим новый чёрный отрезок
        segments[x] = (y, 'B')
        black_total += (y - x)
        black_count += 1

        # Слить с предыдущим?
        i = segments.bisect_left(x)
        if i > 0:
            l2 = segments.iloc[i - 1]
            r2, c2 = segments[l2]
            if r2 == x and c2 == 'B':
                # слить
                segments.pop(l2)
                segments.pop(x)
                segments[l2] = (y, 'B')
                black_count -= 1  # слили два в один

        # Слить с последующим?
        i = segments.bisect_left(x)
        if i + 1 < len(segments):
            l2 = segments.iloc[i + 1]
            r2, c2 = segments[l2]
            l1 = segments.iloc[i]
            r1, c1 = segments[l1]
            if r1 == l2 and c2 == 'B':
                segments.pop(l1)
                segments.pop(l2)
                segments[l1] = (r2, 'B')
                black_count -= 1

    print(black_count, black_total)
