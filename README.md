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


### 10. Поиск обратного пути от текущей вершины (из задачи 3.3)
Т.е мы начинаем идти с нижней вершины и идём до тех пор, пока не достигнем -1 - это является корневой (самой верхней вершиной в дереве)
```python
# Добавляем корень дерева (вершину 0) в массив предков
# Теперь datas = [-1, 0, 0, 1, 1], где datas[0] = -1 (корень не имеет предка)
datas.insert(0, -1)

# Функция для поиска пути от вершины u до корня
def search_path(u, datas):
    path = []  # Список для хранения пути
    # Поднимаемся от вершины u до корня
    while u != -1:
        path.append(u)  # Добавляем текущую вершину в путь
        u = datas[u]    # Переходим к предку
    return path

```

# 4 Контест

### 11. Префиксная сумма для матрицы (из задачи 4.2)
Находим заранее сумму для каждого прямоугольника в матрице. К примеру нашли преф сумму для прямоугольника с координатами y1=1; x1 = 1; y2 = 3; x2 = 3; Сделали это за счёт складывания предыдущих суммы из преф. сумм и добавляем текущее число [i][j]
И потом начинаем выводить для координат прямоугольника его преф сумму, при этом считаем по такому правилу, что вычитаем "лишние" прямоугольники, которые лежат выше необходимого, и добавляем пересечение "лишних" прямоугольников
```python
# Заполняем префиксную матрицу по следующей формуле:
# pref_sum_matrix[i][j] = сумма элементов матрицы от (1,1) до (i,j)
for i in range(1, n + 1):  # идем по строкам
    for j in range(1, m + 1):  # идем по столбцам
        # Считаем текущую префиксную сумму:
        # берем значение сверху, слева, вычитаем угол и прибавляем значение из исходной матрицы
        pref_sum_matrix[i][j] = (pref_sum_matrix[i-1][j] 
                                 + pref_sum_matrix[i][j-1] 
                                 - pref_sum_matrix[i-1][j-1] 
                                 + matrixx[i-1][j-1])

# Обработка запросов
for request in requests:
    # Распаковываем координаты для текущего запроса
    y1, x1, y2, x2 = request
    
    # Используем формулу для вычисления суммы элементов в заданной подматрице
    # S(y1, x1, y2, x2) = S(y2, x2) - S(y1-1, x2) - S(y2, x1-1) + S(y1-1, x1-1)
    result = (pref_sum_matrix[y2][x2] 
              - pref_sum_matrix[y1-1][x2] 
              - pref_sum_matrix[y2][x1-1] 
              + pref_sum_matrix[y1-1][x1-1])
    
    # Вывод результата для текущего запроса
    print(result)

```

### 12. Бинарный поиск и жадный алгоритм для нахождения максимального расстояния между несколькими объектами (из задачи 4.3)
Сначала проходимся по бинарному поиску и ищем максимально возможное расстояние при котором будет выполняться жадный алгоритм, в котором мы пытаемся расставить коров по стойлам с расстоянием, которое передаём из функции бинарного поиска (значение mid).
И если получается расставить пытаемся увеличить значение mid и тем самым попытаться найти большее расстояние между стойлами
```python
# Функция для проверки, можно ли расставить k коров с минимальным расстоянием mid
def check_cows(stoila, k, mid):
    # Позиция последней поставленной коровы (начинаем с первого стойла)
    last_cow_position = stoila[0]
    # Количество уже поставленных коров (начальное значение — 1, так как первую корову уже поставили)
    placed_cow = 1

    # Проходим по всем стойлам, начиная со второго
    for i in range(1, n):
        # Если расстояние от последней коровы до текущего стойла >= mid,
        # то можно поставить корову в это стойло
        if stoila[i] - last_cow_position >= mid:
            # Обновляем позицию последней коровы
            last_cow_position = stoila[i]
            # Увеличиваем количество поставленных коров
            placed_cow += 1

            # Если удалось поставить всех k коров, возвращаем True
            if placed_cow == k:
                return True

    # Если не удалось поставить всех k коров, возвращаем False
    return False

# Функция для выполнения бинарного поиска по ответу
def binary_check(stoila):
    # Левая граница бинарного поиска (минимальное возможное расстояние)
    left = 0
    # Правая граница бинарного поиска (максимальное возможное расстояние)
    right = stoila[-1] - stoila[0]

    # Бинарный поиск: продолжаем, пока левая граница не превысит правую
    while left <= right:
        # Вычисляем середину диапазона (текущее расстояние для проверки)
        mid = (left + right) // 2

        # Проверяем, можно ли расставить k коров с расстоянием mid
        if check_cows(stoila, k, mid) == True:
            # Если можно, пробуем увеличить расстояние (сдвигаем левую границу)
            left = mid + 1
        else:
            # Если нельзя, уменьшаем расстояние (сдвигаем правую границу)
            right = mid - 1

    # По завершении бинарного поиска right содержит максимальное допустимое расстояние
    return right

```


### 13. Сканирующая прямая (из задачи 4.6)
Основная суть алгоритма это в записи отрезков и их дальнейшей сортировки для удобства решения.
Сначала мы считываем и последовательно записываем начало и конец отрезка.
Потом сортируем по началу
И потом уже можно на основании этого массива с отрезками решать любую задачу
В данной задаче нужно найти общую длину всех отрезков. 
Можно находить максимальное количество одновременных отрезков в одной координате и выводить саму координату и кол-во отрезков. Или использовать в других задачах с отрезками (наслаивать на уже отсортированный масив) или добавлять доп. значения при его записи
```python
# Заполняем список отрезков
for i in range(n):
    # Считываем координаты отрезка (начало и конец)
    otrezok = [int(x) for x in sys.stdin.readline().split()]
    start = otrezok[0]  # Начало отрезка
    end = otrezok[1]    # Конец отрезка
    otrezki.append([start, end])  # Добавляем отрезок в список

# Сортируем отрезки по начальной координате (по возрастанию)
otrezki.sort()

# Инициализируем переменные для хранения текущего объединённого отрезка
current_start = otrezki[0][0]  # Начало текущего объединённого отрезка
current_end = otrezki[0][1]    # Конец текущего объединённого отрезка

# Инициализируем переменную для хранения общей длины окрашенной части
summ = 0

# Проходим по всем отрезкам, начиная со второго (индекс 1)
for i in range(1, n):
    # Текущий отрезок
    otrezok_tek = otrezki[i]
    start = otrezok_tek[0]  # Начало текущего отрезка
    end = otrezok_tek[1]    # Конец текущего отрезка

    # Проверяем, пересекается ли текущий отрезок с объединённым отрезком
    if start <= current_end:
        # Если пересекается, обновляем конец объединённого отрезка
        current_end = max(current_end, end)
    else:
        # Если не пересекается, добавляем длину объединённого отрезка к сумме
        summ += (current_end - current_start)
        # Начинаем новый объединённый отрезок
        current_start = start
        current_end = end

# Добавляем длину последнего объединённого отрезка к сумме
summ += (current_end - current_start)
```
P.S чаще всего задачи с отрезками решаются за O(n) (за линию)

#Контест 5

### 14. Сравнение подстрок (из задачи 5.1)
В этой задаче использовали префиксную сумму подстрок
Находил хэши подстрок (преф хэши) через умножение на k^i (любой кэфф, лучше больше и простое число) в степени номера буквы и брал остаток от деления на оч. большое число
Тем самым я заранее нашёл хэш значения для подстрок (они всегда будут одинаковы для одинаковых значений) и сохранил их в преф суммы
Далее я прошёлся по запросам, где записаны индексы начала и конец подстрок, которые нужно сравнить
И там уже, как в обычной преф сумме находил диапазоны от a до b и от c до d, только с учётом умножения на заранее посчитанный захэшированный коэфф k. Он (k) позволяет найти смещение одной подстроки относительно другой (т.к они будут в разных местах строки, а засчёт домножения на фиксированный кэфф итоговые значения хэша подстроки будут совпадать и как бы находится на одинаковых уровнях)

```python
# Инициализация массивов для префиксных сумм и степеней k
pref_summi = [0] * (n + 1)  # Префиксные суммы хэшей
power = [1] * (n + 1)  # Степени k для корректировки хэшей

# Заполнение массивов power и pref_summi
for i in range(n):
    bukva = s[i]  # Текущий символ строки
    index_i = alfavit[bukva]  # Порядковый номер символа в алфавите
    power[i + 1] = (power[i] * k) % MOD  # Вычисление следующей степени k с учётом модуля
    pref_summi[i + 1] = (pref_summi[i] + index_i * power[i]) % MOD  # Обновление префиксной суммы хэшей

# Обработка запросов
for request in requests:
    # Преобразование индексов из 1-индексации в 0-индексацию
    a = request[0] - 1  # Начало первой подстроки
    b = request[1]  # Конец первой подстроки (без вычитания 1, так как префиксные суммы включают правую границу)
    c = request[2] - 1  # Начало второй подстроки
    d = request[3]  # Конец второй подстроки (без вычитания 1)

    # Проверка, равны ли длины подстрок
    if (b - a) != (d - c):
        print("No")  # Если длины разные, подстроки не могут быть равны
        continue

    # Вычисление разницы в позициях подстрок
    if a <= c:
        difference = c - a  # Разница в позициях, если первая подстрока начинается раньше
        first_hash = ((pref_summi[b] - pref_summi[a]) * power[difference]) % MOD  # Хэш первой подстроки с учётом разницы
        second_hash = (pref_summi[d] - pref_summi[c]) % MOD  # Хэш второй подстроки
    else:
        difference = a - c  # Разница в позициях, если вторая подстрока начинается раньше
        first_hash = (pref_summi[b] - pref_summi[a]) % MOD  # Хэш первой подстроки
        second_hash = ((pref_summi[d] - pref_summi[c]) * power[difference]) % MOD  # Хэш второй подстроки с учётом разницы

    # Сравнение хэшей и вывод результата
    if first_hash == second_hash:
        print('Yes')  # Подстроки равны
    else:
        print('No')  # Подстроки не равны

```

### 15. Поиск подстрок в строке (из задачи 5.2)
Основная идея в заранее посчитанных префиксах у каждого элемента подстрок.
Т.е мы проходимся по подстрокам и для каждого элемента ищем количество вхождений ранее и если элементы равны к текущему префиксу добавляем +1, если не равны откатываемся назад на уже ранее посчитанный префикс и так считаем для каждого элемента количество совпадений (длину) относительно строки с которой мы сравниваем 
1. Префиксная функция:
Для подстроки si вычисляем массив pi, где pi[i] — длина наибольшего префикса si[0..i], который является её суффиксом.
Пример для si = "abab": pi = [0, 0, 1, 2]
2. Поиск вхождений:
Проходим по строке T и сравниваем символы с подстрокой si.
Если символы совпадают, увеличиваем счётчик совпадений.
Если символы не совпадают, откатываемся назад, используя префиксную функцию.
Если найдено полное совпадение, сохраняем индекс начала вхождения
3. Обработка запросов:
Если длина si больше длины T, вхождений нет.
Если длина si равна длине T, проверяем, совпадают ли строки.
Иначе используем KMP для поиска всех вхождений.
```python
def prefix_function(s):
    m = len(s)
    pi = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi

def kmp_search(text, pattern, pi):
    n = len(text)
    m = len(pattern)
    j = 0
    occurrences = []
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            occurrences.append(i - m + 1)
            j = pi[j - 1]
    return occurrences

def main():
    T = input().strip()
    q = int(input())
    for _ in range(q):
        si = input().strip()
        m = len(si)
        n = len(T)
        if m > n:
            print(0)
            continue
        if m == n:
            if si == T:
                print(1, 0)
            else:
                print(0)
            continue
        pi = prefix_function(si)
        occurrences = kmp_search(T, si, pi)
        print(len(occurrences), end='')
        if occurrences:
            print(' ' + ' '.join(map(str, occurrences)), end='')
        print()

if __name__ == "__main__":
    main()

```

### 16. Z-функция. Подсчёт длинны совпадения с самого символа до конца совпадения с изначальным префиксом (из задачи 5.5)
Пошаговое объяснение работы алгоритма Z-функции:
1. Инициализация:
Создаём массив z, где будем хранить значения функции (изначально все нули).
Устанавливаем границы текущего "самого правого совпадения" l и r в 0.

2. Основной цикл (идём по строке слева направо, начиная с 1-го индекса):
Для каждого символа i выполняем:

3.Использование предыдущих вычислений (если i внутри известного совпадения):
Если текущая позиция i ≤ r (попадает в ранее найденный совпадающий отрезок):
Берем значение z[i-l] (зеркальной позиции в начале строки).
Но не выходим за границу r, беря минимум с r-i+1.

4. Явное сравнение символов ("развёртывание"):
Сравниваем символы дальше текущего известного совпадения.
Пока символы new_str[z[i]] (начало строки) и new_str[i+z[i]] (текущая позиция) совпадают:
Увеличиваем значение z[i].

5. Обновление границ самого правого совпадения:
Если текущее совпадение (i + z[i] - 1) выходит за известную границу r:
Сдвигаем границы l и r до этого нового совпадения.

Как это работает на практике:
Алгоритм поддерживает "окно" [l,r] самого правого найденного совпадения с префиксом.
Для каждой новой позиции сначала пытается использовать уже вычисленную информацию (чтобы не делать лишних сравнений).
Затем "развёртывает" совпадение, явно сравнивая символы за пределами известной области.
При нахождении большего совпадения обновляет границы "окна".
```python
z = [0]*new_n

l = 0
r = 0

for i in range(1, new_n):
    if i <= r:
        z[i] = min(z[i-l],r - i + 1)
    
    while i + z[i] < new_n and new_str[z[i]] == new_str[z[i]+i]:
        z[i] += 1

    if z[i] + i - 1 > r:
        l = i
        r = z[i] + i - 1
```
