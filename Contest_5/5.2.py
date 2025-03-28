# Читаем строку T и удаляем лишние пробелы (если есть)
t = input().strip()

# Читаем количество запросов q
q = int(input())

# Вычисляем длину строки T
n = len(t)

def prefix_function(s):
    """
    Вычисляет префиксную функцию для строки s.
    Префиксная функция pi[i] — это длина наибольшего собственного префикса строки s[0..i],
    который одновременно является её суффиксом.
    """
    m = len(s)
    pi = [0] * m  # Создаём массив для хранения значений префиксной функции
    j = 0  # Переменная для хранения длины текущего совпадающего префикса

    # Проходим по всем символам строки s, начиная со второго (индекс 1)
    for i in range(1, m):
        # Пока j > 0 и символы не совпадают, откатываемся назад
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]  # Используем уже вычисленные значения префиксной функции
        
        # Если символы совпали, увеличиваем j
        if s[i] == s[j]:
            j += 1
        
        # Записываем значение префиксной функции для текущего индекса
        pi[i] = j
    
    return pi

# Обрабатываем каждый запрос
for _ in range(q):
    # Читаем подстроку s и удаляем лишние пробелы
    s = input().strip()
    m = len(s)  # Длина подстроки s

    # Если длина подстроки больше длины текста, вхождений быть не может
    if m > n:
        print(0)  # Выводим 0 и переходим к следующему запросу
        continue

    # Если длина подстроки равна длине текста, проверяем, совпадают ли строки
    if m == n:
        if s == t:
            print(1, 0)  # Если строки совпадают, выводим 1 и индекс 0
        else:
            print(0)  # Если строки не совпадают, выводим 0
        continue

    # Основной случай: длина подстроки меньше длины текста
    # Вычисляем префиксную функцию для подстроки s
    pi = prefix_function(s)

    # Список для хранения индексов вхождений
    occurrences = []
    j = 0  # Переменная для хранения длины совпавшего префикса

    # Проходим по всем символам текста T
    for i in range(n):
        # Пока есть несовпадение, откатываемся назад по префиксной функции
        while j > 0 and t[i] != s[j]:
            j = pi[j - 1]
        
        # Если символы совпали, увеличиваем j
        if t[i] == s[j]:
            j += 1
        
        # Если j равно длине подстроки s, значит, мы нашли полное вхождение
        if j == m:
            # Добавляем индекс начала вхождения в список
            occurrences.append(i - m + 1)
            # Сдвигаемся для поиска следующего вхождения
            j = pi[j - 1]
    
    # Выводим количество вхождений
    print(len(occurrences), end='')
    # Если вхождения есть, выводим их индексы
    if occurrences:
        print(' ' + ' '.join(map(str, occurrences)), end='')
    # Переход на новую строку для следующего запроса
    print()