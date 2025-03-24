# Определяем константы для двойного хеширования
MOD1 = 10**18 + 3  # Первый большой модуль для уменьшения коллизий
BASE1 = 911382629   # Первая база для хеширования
MOD2 = 10**9 + 7    # Второй модуль (меньше первого)
BASE2 = 35714285    # Вторая база для хеширования

# Читаем входные строки
a = input().strip()  # Основная строка (в задаче это единственная строка)
b = input().strip()  # В задаче не используется, можно игнорировать

n = len(b)  # Длина строки b (в задаче не используется)
m = len(a)  # Длина входной строки

# Проверка на пустую строку или когда длина a меньше b
if n == 0 or m < n:
    print(0)
    exit()

# Вычисляем максимальную длину для предварительного вычисления степеней
max_len = max(2 * n, m)  # Достаточно для всех операций

# Предварительно вычисляем степени BASE1 и BASE2 по модулям
pow_base1 = [1] * (max_len + 1)  # pow_base1[i] = BASE1^i % MOD1
pow_base2 = [1] * (max_len + 1)  # pow_base2[i] = BASE2^i % MOD2
for i in range(1, max_len + 1):
    pow_base1[i] = (pow_base1[i-1] * BASE1) % MOD1
    pow_base2[i] = (pow_base2[i-1] * BASE2) % MOD2

# Функция для вычисления префиксных хешей строки
def compute_prefix_hashes(s, base, mod):
    prefix = [0] * (len(s) + 1)  # prefix[0] = 0, prefix[i] - хеш первых i символов
    for i in range(len(s)):
        # Новый хеш = (старый хеш * base + код символа) % mod
        prefix[i+1] = (prefix[i] * base + ord(s[i])) % mod
    return prefix

# Создаем строку c = b + b (в задаче не используется)
c = b + b

# Вычисляем хеши для строки c (в задаче не используется)
hash_c1 = compute_prefix_hashes(c, BASE1, MOD1)
hash_c2 = compute_prefix_hashes(c, BASE2, MOD2)

# Множество для хранения хешей всех циклических сдвигов b (не используется)
cyclic_hashes = set()
for k in range(n):
    # Вычисляем хеш подстроки c[k..k+n-1] - это k-й циклический сдвиг b
    h1 = (hash_c1[k + n] - hash_c1[k] * pow_base1[n]) % MOD1
    h2 = (hash_c2[k + n] - hash_c2[k] * pow_base2[n]) % MOD2
    cyclic_hashes.add((h1, h2))

# Вычисляем хеши для основной строки a
hash_a1 = compute_prefix_hashes(a, BASE1, MOD1)
hash_a2 = compute_prefix_hashes(a, BASE2, MOD2)

# Счетчик совпадений (в задаче не используется)
count = 0
for i in range(m - n + 1):
    # Хеш подстроки a[i..i+n-1]
    h1 = (hash_a1[i + n] - hash_a1[i] * pow_base1[n]) % MOD1
    h2 = (hash_a2[i + n] - hash_a2[i] * pow_base2[n]) % MOD2
    if (h1, h2) in cyclic_hashes:
        count += 1

print(count)  # В задаче нужно вывести минимальный сдвиг, а не количество