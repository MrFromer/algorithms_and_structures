import sys
input = sys.stdin.readline  # Оптимизация ввода для больших объемов данных

# Чтение n — количество моментов времени (длина массива логов)
# m — количество запросов
n, m = map(int, input().split())

# Считываем количество логов в каждый момент времени
logs_moments = list(map(int, input().split()))

# Создаем массив для хранения дерева отрезков
# Его размер — 4*n, чтобы гарантированно вместить все вершины
trees = [0] * (4 * n)


# -------------------------------
# ФУНКЦИЯ ПОСТРОЕНИЯ ДЕРЕВА
# -------------------------------
def stroim_derevo(v, tl, tr):
    """
    v  — индекс текущей вершины в массиве trees
    tl — левая граница отрезка, которую покрывает вершина
    tr — правая граница отрезка

    Эта функция рекурсивно строит дерево: от листьев к корню.
    """
    if tl == tr:
        # Если отрезок состоит из одного элемента — лист дерева
        trees[v] = logs_moments[tl]
    else:
        # Делим отрезок пополам
        middle = (tl + tr) // 2

        # Строим левое поддерево
        stroim_derevo(v * 2 + 1, tl, middle)

        # Строим правое поддерево
        stroim_derevo(v * 2 + 2, middle + 1, tr)

        # Пересчитываем сумму для текущей вершины
        trees[v] = trees[v * 2 + 1] + trees[v * 2 + 2]


# -------------------------------
# ФУНКЦИЯ ИЗМЕНЕНИЯ ЗНАЧЕНИЯ
# -------------------------------
def change_derevo(v, tl, tr, pos, val):
    """
    Меняет значение в массиве логов в позиции pos на val,
    и пересчитывает все родительские вершины, которые влияют на это значение.
    """
    if tl == tr:
        # Лист дерева: непосредственно меняем значение
        trees[v] = val
    else:
        middle = (tl + tr) // 2

        # Определяем, в какой половине находится нужная позиция
        if pos <= middle:
            change_derevo(v * 2 + 1, tl, middle, pos, val)
        else:
            change_derevo(v * 2 + 2, middle + 1, tr, pos, val)

        # После изменения пересчитываем сумму текущей вершины
        trees[v] = trees[v * 2 + 1] + trees[v * 2 + 2]


# -------------------------------
# ФУНКЦИЯ ПОЛУЧЕНИЯ СУММЫ НА ОТРЕЗКЕ
# -------------------------------
def summa_dereva(v, tl, tr, l, r):
    """
    Возвращает сумму логов на отрезке [l, r]
    v  — текущая вершина
    tl — левая граница сегмента, который она покрывает
    tr — правая граница
    l и r — границы запроса
    """
    if l > r:
        return 0  # пустой отрезок

    if tl == l and tr == r:
        # Если текущий отрезок идеально совпадает с запросом
        return trees[v]

    # Разбиваем запрос и идём в обе половины
    middle = (tl + tr) // 2

    # Левая часть запроса
    left_sum = summa_dereva(v * 2 + 1, tl, middle, l, min(r, middle))

    # Правая часть запроса
    right_sum = summa_dereva(v * 2 + 2, middle + 1, tr, max(l, middle + 1), r)

    return left_sum + right_sum


# Построили дерево на основе изначального массива логов
stroim_derevo(0, 0, n - 1)


# -------------------------------
# ОБРАБОТКА ЗАПРОСОВ
# -------------------------------
for _ in range(m):
    line = list(map(int, input().split()))
    type = line[0]

    if type == 1:
        # Запрос на изменение: "1 i v" — изменить i-й лог на значение v
        i, v = line[1], line[2]
        change_derevo(0, 0, n - 1, i, v)

    elif type == 2:
        # Запрос на сумму: "2 l r" — найти сумму логов на отрезке [l, r-1]
        l, r = line[1], line[2]
        print(summa_dereva(0, 0, n - 1, l, r - 1))  # Важно: r-1, потому что r не включается


#оптимизированная версия
# import sys

# # Чтение всех данных сразу
# data = sys.stdin.read().split()
# ptr = 0

# n = int(data[ptr])
# ptr += 1
# m = int(data[ptr])
# ptr += 1

# logs = list(map(int, data[ptr:ptr + n]))
# ptr += n

# # Инициализация дерева отрезков
# size = 1
# while size < n:
#     size <<= 1
# tree = [0] * (2 * size)

# # Построение дерева (итеративно)
# for i in range(n):
#     tree[size + i] = logs[i]
# for i in range(size - 1, 0, -1):
#     tree[i] = tree[2 * i] + tree[2 * i + 1]

# # Обработка запросов
# output = []
# for _ in range(m):
#     cmd = data[ptr]
#     ptr += 1
    
#     if cmd == '1':
#         # Обновление элемента
#         pos = int(data[ptr])
#         ptr += 1
#         val = int(data[ptr])
#         ptr += 1
        
#         # Обновляем лист
#         pos += size
#         tree[pos] = val
#         # Поднимаемся к корню
#         pos >>= 1
#         while pos >= 1:
#             new_val = tree[2 * pos] + tree[2 * pos + 1]
#             if tree[pos] == new_val:
#                 break
#             tree[pos] = new_val
#             pos >>= 1
            
#     elif cmd == '2':
#         # Запрос суммы [l, r)
#         l = int(data[ptr])
#         ptr += 1
#         r = int(data[ptr])
#         ptr += 1
#         res = 0
        
#         l += size
#         r += size - 1  # Преобразуем [l, r) в [l, r-1]
        
#         while l <= r:
#             if l % 2 == 1:
#                 res += tree[l]
#                 l += 1
#             if r % 2 == 0:
#                 res += tree[r]
#                 r -= 1
#             l >>= 1
#             r >>= 1
            
#         output.append(str(res))

# # Вывод всех результатов
# print('\n'.join(output))