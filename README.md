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
