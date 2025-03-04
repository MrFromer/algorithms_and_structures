For myself education repo, algorithms for futer projects and my notes

# 1 Контест

### 1. Бинарный поиск

Помогает найти нужное число, путём отрезания половинок, при сравнении с самим числом, если нужно число лежит левее, мы срезаем правую часть и если искомое число лежит справа, срезаем левую часть
Время O(logn)

```python
def binary_check(n,arr,target):
    left, right = 0, n-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1

    return False
```

### 2. Сортировка слиянием (по принципу разделяй и властвуй)
Помогает отсортировать за n*log(n) с использованием двух функций

```python
def merge_sort(arr):
    # Базовый случай: если массив состоит из одного элемента или пуст
    if len(arr) <= 1:
        return arr, 0

    # Находим середину массива
    mid = len(arr) // 2

    # Рекурсивно сортируем левую и правую половины
    left, inv_left = merge_sort(arr[:mid])
    right, inv_right = merge_sort(arr[mid:])

    # Сливаем две отсортированные половины и считаем инверсии
    merged, inv_merge = merge(left, right)

    # Общее количество инверсий
    total_inv = inv_left + inv_right + inv_merge

    return merged, total_inv

def merge(left, right):
    result = []
    i = j = 0
    inv_count = 0

    # Слияние двух отсортированных массивов
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            # Все оставшиеся элементы в левой половине образуют инверсии с right[j]
            inv_count += len(left) - i

    # Добавляем оставшиеся элементы (если они есть)
    result.extend(left[i:])
    result.extend(right[j:])

    return result, inv_count

# Чтение входных данных
n = int(input())
arr = list(map(int, input().split()))

# Сортировка и подсчёт инверсий
sorted_arr, inversions = merge_sort(arr)

# Вывод результата
print(inversions)
print(" ".join(map(str, sorted_arr)))
```
### 3. Составление полиндрома с учётом алфавитного порядка
Создаём полиндром через словарь, если у нас чётное кол-во букв раскидываем их по бокам (слева-справа), если нечётная и середины свободна, добавляем туда, иначе возвращаем одну букву т.к нельзя составить полиндром

``` python
n = int(input())
s = input().strip()

# Подсчет частот букв без Counter
freq = {}
for char in s:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

# Формирование палиндрома
left_part = []
center = ""

# Сортируем ключи вручную через sorted
for char in sorted(freq):
    count = freq[char]
    left_part.append(char * (count // 2))  # левая часть палиндрома
    if count % 2 == 1 and center == "":  # центральный символ (если нечетное кол-во)
        center = char

# Собираем палиндром
left = "".join(left_part)
result = left + center + left[::-1]

# Выводим результат
print(result)
```

# 2 Контест

### 4. Поиск минимального числа в окне чисел (выбираем min число из нескольких k чисел) при помощи двух стеков \
Идея: 1) Создаём два стека, где сначала заполняем первый стек, как только он переполняется, начинаем переносить самый первый элемент во второй стек (как в очереди, кто пришёл самым первым, уйдёт самым первым) \
2) И после того, как добавили самый первый элемент во второй стек, удаляем его из первого стека и уже вносим след числа в него \
3) Если мы достигли такой точки (такого числа i), когда кол-во элементов больше k (т.е выпл. условие), мы начинаем выбирать минимальные элементы из k чисел, при помощи стеков, где у нас в самом конце стеков лежат минимальные значения, мы выбираем наименьшее из прошлого диапазона k и нового числа, который добавили в первый стек \
4) И так делаем по циклу, пока не пройдём все числа \
По итогу получаем алгоритм со сложностью примерно **O(n)**

```python
# Считываем два числа: n (длина массива) и k (размер окна)
n, k = [int(x) for x in input().split()]

# Считываем массив чисел
mass = [int(x) for x in input().split()]

# Инициализируем два стека:
# stack1 - для хранения элементов, которые добавляются в текущее окно
# stack2 - для хранения элементов, которые перемещаются из stack1 при сдвиге окна
stack1 = []  # Первый стек (вход)
stack2 = []  # Второй стек (выход)

# Инициализируем список для хранения минимальных значений в каждом окне
result_min = []

# Функция для добавления элемента в стек
def push(stack, value):
    # Если стек пуст, добавляем элемент и указываем, что он же является минимальным
    if not stack:
        stack.append((value, value))  # (элемент, минимум)
    # Если стек не пуст, добавляем элемент и обновляем минимум
    else:
        stack.append((value, min(value, stack[-1][1])))

# Функция для извлечения элемента из стека
def pop(stack):
    # Удаляем последний элемент из стека и возвращаем его значение (первый элемент кортежа)
    return stack.pop()[0]

# Функция для получения минимального значения в текущем окне
def print_min():
    # Если оба стека пусты, возвращаем None (этот случай не должен происходить в корректной работе)
    if not stack2 and not stack1:
        return None
    # Если stack1 пуст, возвращаем минимум из stack2
    if not stack1:
        return stack2[-1][1]
    # Если stack2 пуст, возвращаем минимум из stack1
    if not stack2:
        return stack1[-1][1]
    # Если оба стека не пусты, возвращаем минимальное значение из двух стеков
    return min(stack1[-1][1], stack2[-1][1])

# Основной цикл: проходим по каждому элементу массива
for i in range(0, n):
    # Если окно переполнено (содержит k элементов), удаляем элемент из stack2
    if i >= k:
        # Если stack2 пуст, переносим все элементы из stack1 в stack2
        if not stack2:
            while stack1:
                push(stack2, pop(stack1))
        # Удаляем элемент из stack2 (элемент, который выходит из окна)
        pop(stack2)

    # Добавляем текущий элемент в stack1
    push(stack1, mass[i])

    # Если окно сформировано (содержит k элементов), добавляем минимум в результат
    if i >= k - 1:
        result_min.append(print_min())

# Выводим результат: минимальные значения для каждого окна, разделенные пробелами
print(*result_min)
```

### 5. Префиксные суммы
Заранее находим все суммы, последовательным сложением элементов (индекс эл. будет совпадать с его преф. суммой)
``` python
n = int(input())
prefix_summ = [0] * (n + 1)
for i in range(n):
    prefix_summ[i + 1] = prefix_summ[i] + datas[i]
```

### 6. Поиск минимального значения слева/справа
Идея в том, чтобы доходить до самого элемента, путём удаления больших элементов с нужной стороны и последний элемент и будет наименьшим с одной стороны относительно того числа к которому мы ищем минимальный элемент
``` python
# Используем стек для нахождения ближайшего меньшего элемента слева
stack = []
for i in range(n):
    # Удаляем из стека все элементы, которые больше или равны текущему элементу
    while stack and datas[stack[-1]] >= datas[i]:
        stack.pop()
    # Если стек не пуст, то ближайший меньший элемент слева — это последний элемент в стеке
    if stack:
        left[i] = stack[-1]
    else:
        # Иначе меньшего элемента слева нет
        left[i] = -1
    # Добавляем текущий индекс в стек
    stack.append(i)

# Создаем массив right для хранения индексов ближайшего меньшего элемента справа
# Изначально заполняем его значениями n (если меньшего элемента нет)
right = [n] * n

# Используем стек для нахождения ближайшего меньшего элемента справа
stack = []
for i in range(n - 1, -1, -1):  # Идем с конца массива в начало
    # Удаляем из стека все элементы, которые больше или равны текущему элементу
    while stack and datas[stack[-1]] >= datas[i]:
        stack.pop()
    # Если стек не пуст, то ближайший меньший элемент справа — это последний элемент в стеке
    if stack:
        right[i] = stack[-1]
    else:
        # Иначе меньшего элемента справа нет
        right[i] = n
    # Добавляем текущий индекс в стек
    stack.append(i)
```

# 3 Контест

### 7. Создание списка смежности в дереве (из задачи 3.1)
Строим список смежности за счёт, того, что на вход подаются индексы (текущий элемент), а в datas[i] содержатся значения к какому родителю относится ребёнок (i+1)
``` python
#        0
#       / \
#      1   2
#     /|\   \
#    3 4 5   6
for i in range(n-1):
    parent = datas[i]
    child = i + 1
    collision_list[parent].append(child)
#Вывод: [[1,2],[3,4,5],[6]]
```

### 8. Поиск глубины для всех элементов в дереве (из задачи 3.1)
Передаём начальный элемент (корневой) с нулевой глубиной и создаём пустой список с нулями для каждого элемента \
И рекурсивно проходимся по всему дереву (сверху-вниз-вверх-вниз и так до конца, пока не пройдём все вершины и не найдём для каждого глубину) \
Для понимания входных данных см. выше и задачу 3.1
``` python
#поиск глубины для каждой вершины
def DFS(versina,depth):
    depths[versina] = depth #заполняю глубину текущей вершины
    for child in collision_list[versina]: #обходим всех детей в каждом радителе и так рекурсивно до конца дерева
        DFS(child,depth+1)
depths = [0]*n
DFS(0,0)
```

#### Интересный способ считывания данных для каждой вершины (берём и записываем для вершины i её детей) (из задачи 3.2)
```python
# Чтение списка детей для каждой вершины
    # children[i] содержит кортеж (left_child, right_child) для вершины i
    # Если left_child или right_child равен -1, это означает, что ребёнок отсутствует
    children = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
```

### 9. Проверка дерева на AVL (из задачи 3.2)
AVL-дерево – это дерево, для которого выполняются следующие условия:
1. оба поддерева – левое и правое – являются AVL-деревьями;
2. все вершины левого поддерева вершины X, меньше самой вершины X;
3. все вершины правого поддерева вершины X, больше самой вершины X;
4. для каждой вершины высота её двух поддеревьев различается не более чем на 1 (высота –
расстояние до самого дальнего листа).
```python
# Функция для проверки, является ли поддерево AVL-деревом
    def is_avl(node, min_val, max_val):
        """
        Рекурсивная функция для проверки, является ли поддерево AVL-деревом.
        :param node: Текущая вершина
        :param min_val: Минимальное допустимое значение для текущей вершины
        :param max_val: Максимальное допустимое значение для текущей вершины
        :return: Кортеж (является ли поддерево AVL-деревом, высота поддерева)
        """
        # Если вершины нет (достигли листа), возвращаем True и высоту 0
        if node == -1:
            return True, 0

        # Проверяем, что значение вершины находится в допустимых границах
        # Для BST: все вершины в левом поддереве должны быть меньше текущей вершины,
        # а все вершины в правом поддереве — больше
        if not (min_val < node < max_val):
            return False, 0

        # Получаем левого и правого ребёнка текущей вершины
        left_child, right_child = children[node]

        # Рекурсивно проверяем левое поддерево
        # Для левого поддерева максимальное значение — текущая вершина (node)
        is_left_avl, left_height = is_avl(left_child, min_val, node)

        # Рекурсивно проверяем правое поддерево
        # Для правого поддерева минимальное значение — текущая вершина (node)
        is_right_avl, right_height = is_avl(right_child, node, max_val)

        # Проверяем сбалансированность поддерева
        # Разница высот левого и правого поддеревьев не должна превышать 1
        if abs(left_height - right_height) > 1:
            return False, 0

        # Если оба поддерева являются AVL-деревьями и сбалансированы,
        # возвращаем True и высоту текущего поддерева
        # Высота поддерева = максимальная высота левого или правого поддерева + 1
        return is_left_avl and is_right_avl, max(left_height, right_height) + 1
```
