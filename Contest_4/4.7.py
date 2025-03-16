import sys

def time_to_seconds(hours, minutes, seconds):
    """Переводит время в секунды от начала суток."""
    return hours * 3600 + minutes * 60 + seconds

# Считываем количество касс
n = int(sys.stdin.readline())

# Создаём список событий
events = []

for _ in range(n):
    # Считываем время открытия и закрытия кассы
    h1, m1, s1, h2, m2, s2 = map(int, sys.stdin.readline().split())
    start = time_to_seconds(h1, m1, s1)  # Время открытия в секундах
    end = time_to_seconds(h2, m2, s2)    # Время закрытия в секундах

    # Если касса работает круглосуточно
    if start == end:
        events.append((0, 1))        # Событие открытия в 00:00:00
        events.append((86400, -1))   # Событие закрытия в 24:00:00
    # Если касса работает через полночь (например, 22:00 до 02:00)
    elif start > end:
        events.append((0, 1))        # Событие открытия в 00:00:00
        events.append((end, -1))     # Событие закрытия в end
        events.append((start, 1))    # Событие открытия в start
        events.append((86400, -1))   # Событие закрытия в 24:00:00
    else:
        # Обычный случай (например, 10:00 до 18:00)
        events.append((start, 1))    # Событие открытия
        events.append((end, -1))     # Событие закрытия

# Сортируем события:
# 1. По времени.
# 2. Если время совпадает, сначала обрабатываем закрытие (-1), затем открытие (+1).
events.sort()

# Инициализируем переменные
active = 0  # Количество активных касс
total_time = 0  # Общее время, когда все кассы работают одновременно
prev_time = 0  # Время предыдущего события

# Проходим по всем событиям
for time, delta in events:
    # Если все кассы активны, добавляем время к total_time
    if active == n:
        total_time += time - prev_time

    # Обновляем количество активных касс
    active += delta

    # Обновляем время предыдущего события
    prev_time = time

# Выводим результат
print(total_time)
