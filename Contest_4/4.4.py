# Считываем входные данные: n (размер таблицы умножения) и k (порядковый номер искомого числа)
n, k = [int(x) for x in input().split()]

# Инициализируем левую границу бинарного поиска (минимальное возможное значение в таблице умножения)
left = 1

# Инициализируем правую границу бинарного поиска (максимальное возможное значение в таблице умножения)
right = n * n

# Основной цикл бинарного поиска: продолжаем, пока левая граница не превысит правую
while left <= right:
    # Вычисляем середину диапазона (текущее число для проверки)
    mid = (left + right) // 2

    # Переменная для подсчёта количества чисел в таблице, которые меньше или равны mid
    summ = 0

    # Проходим по всем строкам таблицы умножения (от 1 до n)
    for i in range(1, n + 1):
        # Для каждой строки i считаем, сколько чисел в этой строке меньше или равно mid
        # Это значение равно min(mid // i, n), так как в строке i числа: i, 2i, 3i, ..., ni
        summ += min(mid // i, n)

    # Если количество чисел, меньших или равных mid, больше или равно k,
    # значит, искомое число находится в левой половине (включая mid)
    if summ >= k:
        # Сдвигаем правую границу влево (ищем меньшее значение)
        right = mid - 1
    else:
        # Иначе искомое число находится в правой половине (исключая mid)
        # Сдвигаем левую границу вправо (ищем большее значение)
        left = mid + 1

# По завершении бинарного поиска left указывает на k-е число в таблице умножения
print(left)