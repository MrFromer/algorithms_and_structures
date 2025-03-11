import sys  # Импорт модуля sys для быстрого ввода через sys.stdin.readline()

# Считываем размер массива n (количество элементов в массиве bank)
n = int(input())

# Считываем массив bank, используя быструю функцию ввода.
# sys.stdin.readline() быстрее, чем input(), и здесь мы разбиваем строку на числа с помощью map(int, ...)
bank = list(map(int, sys.stdin.readline().split()))

# Считываем количество запросов m
m = int(input())

# Пример входных данных:
# n = 5
# bank = [3, 1, 8, 7, 3]
# m = 3
# Запросы:
# 2 1 2  -> XOR на отрезке [1, 2]
# 1 3 4  -> Сумма на отрезке [3, 4]
# 1 3 3  -> Сумма на отрезке [3, 3]

# ---------------------- Префиксные суммы ----------------------

# Создаем массивы для хранения префиксных сумм:
# prefs_sum[i] — сумма элементов с 1 по i включительно
# prefs_sum_XOR[i] — побитовый XOR элементов с 1 по i включительно

# Размер n + 1, потому что 0-й элемент — это технический 0, чтобы можно было удобно считать отрезки
prefs_sum = [0] * (n + 1)
prefs_sum_XOR = [0] * (n + 1)

# Заполняем префиксные суммы и префиксные XOR
# prefs_sum[i] = prefs_sum[i-1] + bank[i-1] — сумма всех элементов от 1 до i
# prefs_sum_XOR[i] = prefs_sum_XOR[i-1] ^ bank[i-1] — XOR всех элементов от 1 до i
for i in range(1, n + 1):
    prefs_sum[i] = prefs_sum[i - 1] + bank[i - 1]  # обычная сумма
    prefs_sum_XOR[i] = prefs_sum_XOR[i - 1] ^ bank[i - 1]  # побитовый XOR

# После этого:
# prefs_sum = [0, 3, 4, 12, 19, 22]
# prefs_sum_XOR = [0, 3, 2, 10, 13, 14]

# ---------------------- Функции для запросов ----------------------

# Функция для вычисления суммы на отрезке [l, r]
# Формула: сумма на отрезке = prefs_sum[r] - prefs_sum[l-1]
def pref_sum(l, r):
    return prefs_sum[r] - prefs_sum[l - 1]

# Функция для вычисления XOR на отрезке [l, r]
# Формула: XOR на отрезке = prefs_sum_XOR[r] ^ prefs_sum_XOR[l-1]
def XOR_2(l, r):
    return prefs_sum_XOR[r] ^ prefs_sum_XOR[l - 1]

# ---------------------- Обработка запросов ----------------------

# Массив для хранения ответов на запросы, чтобы не печатать их по одному (ускоряет вывод)
output = []

# Читаем m запросов
for _ in range(m):
    # Считываем запрос: movement — тип запроса (1 = сумма, 2 = XOR), l и r — границы отрезка
    movement, l, r = map(int, sys.stdin.readline().split())

    # Если запрос — сумма (movement == 1), вызываем pref_sum и добавляем результат в output
    if movement == 1:
        output.append(str(pref_sum(l, r)))

    # Если запрос — XOR (movement == 2), вызываем XOR_2 и добавляем результат в output
    elif movement == 2:
        output.append(str(XOR_2(l, r)))

# Печатаем все результаты за один раз, используя '\n'.join()
# Это быстрее, чем печатать их по одному через print() в цикле
print('\n'.join(output))





#Чисто решил запариться и посчитать XOR для двух чисел ручками
#вручную считаем XOR (исключающее ИЛИ) для двух чисел и выводим числовой результат Искл. ИЛИ от двух чисел
# def XOR(l,r):
#     first = bin(bank[l-1])[2:]
#     second = bin(bank[r-1])[2:]

#     max_len = max(len(first),len(second))
#     first = first.zfill(max_len)
#     second = second.zfill(max_len)

#     result = ''
#     for i in range(len(first)):
#         if int(first[i]) != int(second[i]):
#             result += '1'
#         else:
#             result += '0'
#     return int(result,2)
    