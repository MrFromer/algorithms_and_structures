def count_palindromic_substrings(s):
    # Преобразуем строку для обработки четных и нечетных палиндромов
    modified = '#' + '#'.join(s) + '#'
    n = len(modified)
    p = [0] * n
    center = right = 0
    total = 0

    for i in range(n):
        # Используем зеркальное отражение, если текущий индекс в пределах правой границы
        if i < right:
            mirror = 2 * center - i
            p[i] = min(right - i, p[mirror])

        # Пытаемся расширить палиндром
        a = i + (1 + p[i])
        b = i - (1 + p[i])
        while a < n and b >= 0 and modified[a] == modified[b]:
            p[i] += 1
            a += 1
            b -= 1

        # Обновляем центр и правую границу, если текущий палиндром выходит за пределы
        if i + p[i] > right:
            center = i
            right = i + p[i]

        # Добавляем количество палиндромов с центром в i
        total += (p[i] + 1) // 2

    return total

def main():
    import sys
    s = sys.stdin.readline().strip()
    print(count_palindromic_substrings(s))

if __name__ == "__main__":
    main()
