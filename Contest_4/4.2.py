import sys

# Считываем три числа: n (количество строк в матрице), m (количество столбцов) и k (количество запросов)
n, m, k = [int(x) for x in sys.stdin.readline().split()]

# Считываем матрицу размером n x m, где каждая строка вводится отдельно
matrixx = [[int(x) for x in sys.stdin.readline().split()] for _ in range(n)]

# Считываем k запросов, где каждый запрос состоит из четырех чисел: y1, x1, y2, x2
requests = [[int(x) for x in sys.stdin.readline().split()] for _ in range(k)]

# Создаем префиксную сумму матрицы размером (n+1) x (m+1)
# Используем n+1 и m+1 для удобства, чтобы границы префиксной суммы легко работали с индексами (1-based)
pref_sum_matrix = [[0] * (m + 1) for _ in range(n + 1)]

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
