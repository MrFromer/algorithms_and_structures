t = input().strip()
q = int(input())
n = len(t)

def prefix_function(s):
    """Корректно вычисляем префиксную функцию для строки s"""
    m = len(s)
    pi = [0] * m
    j = 0
    for i in range(1, m):  # Исправлено: обрабатываем все символы строки s
        while j > 0 and s[i] != s[j]:
            j = pi[j-1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi

for _ in range(q):
    s = input().strip()
    m = len(s)
    
    # Обработка случая, когда подстрока длиннее текста
    if m > n:
        print(0)
        continue
    
    # Случай, когда подстрока равна тексту
    if m == n:
        if s == t:
            print(1, 0)
        else:
            print(0)
        continue
    
    # Основной алгоритм KMP для m < n
    pi = prefix_function(s)
    occurrences = []
    j = 0
    
    for i in range(n):  # Исправлено: обрабатываем все символы текста t
        while j > 0 and t[i] != s[j]:
            j = pi[j-1]
        if t[i] == s[j]:
            j += 1
        if j == m:
            occurrences.append(i - m + 1)
            j = pi[j-1]  # Сдвигаемся для поиска следующих вхождений
    
    print(len(occurrences), end='')
    if occurrences:
        print(' ' + ' '.join(map(str, occurrences)), end='')
    print()