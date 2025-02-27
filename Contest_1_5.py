def f(a, b, c, d, x):
    return a * x**3 + b * x**2 + c * x + d

def find_root(a, b, c, d):
    left = -1e6
    right = 1e6
    precision = 1e-8  # Точность для 4 знаков после точки

    while right - left > precision:
        mid = (left + right) / 2
        value = f(a, b, c, d, mid)

        if value == 0:
            return mid
        elif f(a, b, c, d, left) * value < 0:
            right = mid
        else:
            left = mid

    return (left + right) / 2

# Чтение входных данных
a, b, c, d = map(int, input().split())

# Поиск корня
root = find_root(a, b, c, d)

# Вывод результата с точностью 4 знака после точки
print("{0:.6f}".format(root))