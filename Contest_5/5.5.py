p = input()
t = input()
new_str = p + '#' + t

n_p = len(p)
n_t = len(t)
new_n = len(new_str)

z = [0]*new_n

l = 0
r = 0

for i in range(1, new_n):
    if i <= r:
        z[i] = min(z[i-l],r - i + 1)
    
    while i + z[i] < new_n and new_str[z[i]] == new_str[z[i]+i]:
        z[i] += 1

    if z[i] + i - 1 > r:
        l = i
        r = z[i] + i - 1

count = 0
vjozdenia = []

for i in range(n_p + 1, new_n):
    # Полное совпадение
    if z[i] == n_p:
        count += 1
        vjozdenia.append(i - n_p - 1 + 1)  # +1 для нумерации с 1
    # Проверка на одно несовпадение
    elif z[i] >= n_p - 1:  # Изменили условие
        # Проверяем возможные варианты с одним несовпадением
        pos_in_t = i - n_p - 1
        mismatches = 0
        for j in range(n_p):
            if pos_in_t + j >= n_t:
                break
            if t[pos_in_t + j] != p[j]:
                mismatches += 1
                if mismatches > 1:
                    break
        if mismatches <= 1:
            count += 1
            vjozdenia.append(pos_in_t + 1)  # +1 для нумерации с 1

print(z)
print(count)
print(vjozdenia)