import sys
input = sys.stdin.readline  # Используем быстрый ввод для больших объемов данных

# ЧТЕНИЕ ВХОДНЫХ ДАННЫХ
# Считываем размер массива (n) и количество запросов (m)
n, m = map(int, input().split())
# Считываем сам массив чисел
arr = list(map(int, input().split()))

# ИНИЦИАЛИЗАЦИЯ ДЕРЕВА ОТРЕЗКОВ
# Создаем массив для хранения дерева отрезков.
# Каждый элемент будет хранить пару (минимальное значение, количество минимумов)
# Размер 4*n - стандартный выбор для полного бинарного дерева
tree = [(0, 0)] * (4 * n)  

def build(v, tl, tr):
    """
    Рекурсивная функция построения дерева отрезков
    v - текущая вершина дерева
    tl, tr - границы текущего отрезка (включительно)
    """
    if tl == tr:
        # Базовый случай - дошли до листа
        # В листе храним сам элемент и количество 1 (так как это единственный элемент)
        tree[v] = (arr[tl], 1)  
    else:
        # Рекурсивно строим левое и правое поддеревья
        tm = (tl + tr) // 2  # Середина отрезка
        build(v*2+1, tl, tm)  # Левое поддерево
        build(v*2+2, tm+1, tr)  # Правое поддерево
        
        # Получаем значения из левого и правого поддеревьев
        left_min, left_cnt = tree[v*2+1]
        right_min, right_cnt = tree[v*2+2]
        
        # Формируем значение для текущей вершины
        if left_min < right_min:
            # Если минимум слева меньше - берем его
            tree[v] = (left_min, left_cnt)
        elif left_min > right_min:
            # Если минимум справа меньше - берем его
            tree[v] = (right_min, right_cnt)
        else:
            # Если минимумы равны - суммируем их количества
            tree[v] = (left_min, left_cnt + right_cnt)

def update(v, tl, tr, pos, new_val):
    """
    Функция обновления значения в массиве
    v - текущая вершина
    tl, tr - границы текущего отрезка
    pos - позиция для обновления
    new_val - новое значение
    """
    if tl == tr:
        # Базовый случай - дошли до нужного листа
        tree[v] = (new_val, 1)
    else:
        tm = (tl + tr) // 2
        if pos <= tm:
            # Если позиция в левом поддереве - идем туда
            update(v*2+1, tl, tm, pos, new_val)
        else:
            # Иначе - в правое поддерево
            update(v*2+2, tm+1, tr, pos, new_val)
        
        # После обновления пересчитываем текущую вершину
        left_min, left_cnt = tree[v*2+1]
        right_min, right_cnt = tree[v*2+2]
        
        if left_min < right_min:
            tree[v] = (left_min, left_cnt)
        elif left_min > right_min:
            tree[v] = (right_min, right_cnt)
        else:
            tree[v] = (left_min, left_cnt + right_cnt)

def query(v, tl, tr, l, r):
    """
    Функция запроса минимума и количества минимумов на отрезке [l, r]
    v - текущая вершина
    tl, tr - границы текущего отрезка в дереве
    l, r - границы запрашиваемого отрезка
    """
    if l > r:
        # Некорректный запрос - возвращаем нейтральный элемент
        return (float('inf'), 0)  # (бесконечность, 0)
    
    if l == tl and r == tr:
        # Если текущий отрезок точно соответствует запросу
        return tree[v]
    
    # Разбиваем запрос на подотрезки
    tm = (tl + tr) // 2
    
    # Рекурсивно запрашиваем левую часть
    left_min, left_cnt = query(v*2+1, tl, tm, l, min(r, tm))
    # Рекурсивно запрашиваем правую часть
    right_min, right_cnt = query(v*2+2, tm+1, tr, max(l, tm+1), r)
    
    # Объединяем результаты
    if left_min < right_min:
        return (left_min, left_cnt)
    elif left_min > right_min:
        return (right_min, right_cnt)
    else:
        return (left_min, left_cnt + right_cnt)

# ПОСТРОЕНИЕ ДЕРЕВА
build(0, 0, n-1)  # Строим дерево для всего массива (от 0 до n-1)

# ОБРАБОТКА ЗАПРОСОВ
output = []  # Буфер для хранения результатов
for _ in range(m):
    parts = input().split()  # Читаем запрос
    if not parts:
        continue  # Пропускаем пустые строки
    
    type_op = parts[0]  # Тип операции
    
    if type_op == '1':
        # Операция обновления
        i, v = map(int, parts[1:])  # Позиция и новое значение
        update(0, 0, n-1, i, v)  # Вызываем функцию обновления
    elif type_op == '2':
        # Операция запроса
        l, r = map(int, parts[1:])  # Границы отрезка
        # Запрашиваем минимум и количество на отрезке [l, r-1]
        min_val, count = query(0, 0, n-1, l, r-1)
        output.append(f"{min_val} {count}")  # Добавляем результат в буфер

# ВЫВОД РЕЗУЛЬТАТОВ
print('\n'.join(output))  # Выводим все результаты одной операцией