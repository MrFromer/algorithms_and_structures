p = input().strip()
t = input().strip()
new_str = p + '#' + t

n_p = len(p)
n_t = len(t)
new_n = len(new_str)

z = [0] * new_n

l = 0
r = 0

# Вычисление Z-функции
for i in range(1, new_n):
    if i <= r:
        z[i] = min(z[i - l], r - i + 1)
    
    while i + z[i] < new_n and new_str[z[i]] == new_str[i + z[i]]:
        z[i] += 1

    if i + z[i] - 1 > r:
        l = i
        r = i + z[i] - 1

count = 0
vjozdenia = []

for i in range(n_p + 1, new_n):
    pos_in_t = i - n_p - 1  # Позиция в строке t
    if pos_in_t < 0:
        continue  # Пропускаем некорректные позиции
    
    # Полное совпадение
    if z[i] == n_p:
        count += 1
        vjozdenia.append(pos_in_t + 1)  # +1 для нумерации с 1
    
    # Проверка на одно несовпадение
    elif z[i] >= n_p - 1:
        # Проверяем только потенциальные проблемные места
        # (не проверяем уже совпавшие символы)
        mismatches = 0
        # Проверяем символы после совпавшего префикса
        for j in range(z[i], n_p):
            if pos_in_t + j >= n_t:  # Проверка выхода за границы
                break
            if t[pos_in_t + j] != p[j]:
                mismatches += 1
                if mismatches > 1:
                    break
        # Проверяем возможную ошибку в начале
        if mismatches <= 1:
            count += 1
            vjozdenia.append(pos_in_t + 1)

# Удаляем дубликаты и сортируем
vjozdenia = sorted(list(set(vjozdenia)))

print(len(vjozdenia))
if vjozdenia:
    print(' '.join(map(str, vjozdenia)))
else:
    print()