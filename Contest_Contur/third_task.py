import sys

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    N = int(input[ptr])
    ptr += 1
    M = int(input[ptr])
    ptr += 1
    s = list(map(int, input[ptr:ptr+N]))
    ptr += N

    # Словарь для хранения границ каждого цвета
    color_ranges = {}
    for idx, color in enumerate(s, 1):  # Используем 1-based индексацию
        if color not in color_ranges:
            color_ranges[color] = [idx, idx]
        else:
            color_ranges[color][0] = min(color_ranges[color][0], idx)
            color_ranges[color][1] = max(color_ranges[color][1], idx)

    # Проверка, что количество цветов не превышает M
    if len(color_ranges) > M:
        print(-1)
        return

    # Проверка, что все вхождения цвета находятся в его диапазоне
    for color, (l, r) in color_ranges.items():
        for i in range(l, r+1):
            if s[i-1] != color:  # Переход к 0-based индексации
                print(-1)
                return

    # Сортируем цвета по правой границе (по убыванию)
    sorted_colors = sorted(color_ranges.items(), key=lambda x: -x[1][1])

    # Проверяем покрытие всех домов
    covered = [False] * (N + 2)  # 1-based индексация
    for color, (l, r) in sorted_colors:
        for i in range(l, r+1):
            covered[i] = True

    if not all(covered[1:N+1]):  # Проверяем дома с 1 по N
        print(-1)
        return

    # Формируем результат
    print(len(sorted_colors))
    for color, (l, r) in sorted_colors:
        print(color, l, r)

solve()