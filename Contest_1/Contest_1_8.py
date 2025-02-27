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
