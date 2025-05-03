# Импорт стандартных библиотек
import sys

# Чтение входных данных
n = int(input())

# Настройка границ координат
MIN = -500000  # Минимальная возможная координата
MAX = 500000   # Максимальная возможная координата
SIZE = MAX - MIN + 1  # Общий диапазон координат (0..1_000_000)

# Инициализация структур данных для дерева отрезков:
# sum_ - суммарная длина черных отрезков в текущем диапазоне
sum_ = [0] * (4 * SIZE)      

# left/right - цвет границ отрезка (0 - белый, 1 - черный)
left = [0] * (4 * SIZE)      
right = [0] * (4 * SIZE)     

# cnt - количество черных отрезков в текущем диапазоне
cnt = [0] * (4 * SIZE)        

# lazy - ленивые обновления (None - нет, 0 - белый, 1 - черный)
lazy = [None] * (4 * SIZE)    

def push(v, l, r):
    """Проталкивание ленивого обновления в дочерние узлы"""
    if lazy[v] is None or l == r:
        return  # Нет обновления или листовой узел
    
    tm = (l + r) // 2  # Середина текущего диапазона
    
    # Левый и правый дочерние узлы
    left_child = 2*v + 1
    right_child = 2*v + 2
    
    # Применяем обновление к левому ребенку
    color = lazy[v]
    lazy[left_child] = color
    left[left_child] = color
    right[left_child] = color
    cnt[left_child] = 1 if color == 1 else 0
    sum_[left_child] = color * (tm - l + 1)
    
    # Применяем обновление к правому ребенку
    lazy[right_child] = color
    left[right_child] = color
    right[right_child] = color
    cnt[right_child] = 1 if color == 1 else 0
    sum_[right_child] = color * (r - tm)
    
    # Сбрасываем флаг обновления текущего узла
    lazy[v] = None

def update(v, tl, tr, l, r, color):
    """Обновление диапазона [l, r] цветом color"""
    # Если текущий диапазон [tl, tr] не пересекается с [l, r]
    if tr < l or tl > r:
        return 
    
    # Проталкиваем отложенные обновления
    push(v, tl, tr)
    
    # Если текущий диапазон полностью внутри [l, r]
    if l <= tl and tr <= r:
        # Устанавливаем новые значения
        sum_[v] = color * (tr - tl + 1)
        left[v] = right[v] = color
        lazy[v] = color
        cnt[v] = 1 if color == 1 else 0
        return 
    
    # Рекурсивное обновление дочерних узлов
    tm = (tl + tr)//2
    update(2*v + 1, tl, tm, l, r, color)   # Левый ребенок
    update(2*v + 2, tm + 1, tr, l, r, color) # Правый ребенок
    
    # Обновление текущего узла на основе детей
    sum_[v] = sum_[2*v + 1] + sum_[2*v + 2]
    left[v] = left[2*v + 1]
    right[v] = right[2*v + 2]
    cnt[v] = cnt[2*v + 1] + cnt[2*v + 2]
    
    # Если соседние отрезки сливаются
    if right[2*v + 1] == 1 and left[2*v + 2] == 1:
        cnt[v] -= 1

# Основной цикл обработки операций
for _ in range(n):
    parts = input().split()
    cmd = parts[0]
    x = int(parts[1])
    length = int(parts[2])
    
    # Преобразование координат в 0-based систему
    L = x - MIN
    R = x + length - 1 - MIN
    
    if cmd == 'W':
        # Покраска в белый
        update(0, 0, SIZE - 1, L, R, 0)
    else:
        # Покраска в черный
        update(0, 0, SIZE - 1, L, R, 1)
    
    # Вывод результатов для корневого узла (вся прямая)
    print(cnt[0], sum_[0])