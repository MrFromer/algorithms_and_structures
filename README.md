For myself education repo, algorithms for futer projects

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

### 4. Поиск минимального числа в окне чисел (выбираем min число из нескольких k чисел) при помощи двух стеков \
Идея: 1) Создаём два стека, где сначала заполняем первый стек, как только он переполняется, начинаем переносить самый первый элемент во второй стек (как в очереди, кто пришёл самым первым, уйдёт самым первым) \
2) И после того, как добавили самый первый элемент во второй стек, удаляем его из первого стека и уже вносим след числа в него \
3) Если мы достигли такой точки (такого числа i), когда кол-во элементов больше k (т.е выпл. условие), мы начинаем выбирать минимальные элементы из k чисел, при помощи стеков, где у нас в самом конце стеков лежат минимальные значения, мы выбираем наименьшее из прошлого диапазона k и нового числа, который добавили в первый стек \
4) И так делаем по циклу, пока не пройдём все числа \
По итогу получаем алгоритм со сложностью примерно ###O(n)

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
