import sys

n, k = [int(x) for x in sys.stdin.readline().split()]
mass = [int(x) for x in sys.stdin.readline().split()]

def greedy_alg(mass, k, mid):
    count = 0
    summ = 0
    for i in range(n):
        if (summ + mass[i]) > mid:  # Если текущая сумма превышает mid
            count += 1  # Начинаем новый отрезок
            summ = mass[i]  # Сбрасываем сумму и начинаем новый отрезок с текущего элемента
        else:
            summ += mass[i]  # Продолжаем текущий отрезок
    if summ > 0:  # Учитываем последний отрезок
        count += 1
    return count <= k  # Возвращаем True, если количество отрезков не превышает k

def binary_search(mass):
    left = max(mass)  # Минимальная возможная сумма (максимальный элемент)
    right = sum(mass)  # Максимальная возможная сумма (сумма всех элементов)
    while left <= right:
        mid = (left + right) // 2
        if greedy_alg(mass, k, mid):  # Если можно разбить на k отрезков с суммой <= mid
            right = mid - 1  # Пробуем уменьшить сумму
        else:
            left = mid + 1  # Увеличиваем сумму
    return left  # Возвращаем минимальную максимальную сумму

print(binary_search(mass))