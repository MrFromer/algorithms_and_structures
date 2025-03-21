import sys

s = input().strip()
n = len(s)
m = int(input())
k = 31  # Простое число для уменьшения коллизий
MOD = 10**18 + 3  # Большое простое число

requests = []
for _ in range(m):
    requests.append(list(map(int, sys.stdin.readline().split())))

# Словарь для индексов букв
alfavit = {chr(i): i - ord('a') + 1 for i in range(ord('a'), ord('z') + 1)}

# Предвычисление степеней k и префиксных хэшей
prefix = [0] * (n + 1)
power = [1] * (n + 1)
for i in range(n):
    power[i+1] = (power[i] * k) % MOD
    prefix[i+1] = (prefix[i] + alfavit[s[i]] * power[i]) % MOD

# Обработка запросов
for req in requests:
    a, b, c, d = req
    # Проверка длины подстрок
    if (b - a) != (d - c):
        print("No")
        continue
    
    a_start = a - 1
    a_end = b
    c_start = c - 1
    c_end = d
    
    # Вычисляем хэши
    hash_a = (prefix[a_end] - prefix[a_start]) % MOD
    hash_c = (prefix[c_end] - prefix[c_start]) % MOD
    
    # Корректируем степени
    if a_start < c_start:
        shift = c_start - a_start
        hash_a = (hash_a * power[shift]) % MOD
    else:
        shift = a_start - c_start
        hash_c = (hash_c * power[shift]) % MOD
    
    print("Yes" if hash_a == hash_c else "No")