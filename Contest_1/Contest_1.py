#1

# n,k = [int(x) for x in input().split()]
# arr = [int(x) for x in input().split()]
# arr_check = [int(x) for x in input().split()]
#
# def binary_check(n,arr,target):
#     left, right = 0, n-1
#     while left <= right:
#         mid = (left+right)//2
#         if arr[mid] == target:
#             return True
#         elif arr[mid] < target:
#             left = mid + 1
#         elif arr[mid] > target:
#             right = mid - 1
#
#     return False
#
# for i in range(k):
#     if binary_check(n,arr,arr_check[i]) == True:
#
#         print('YES')
#     elif binary_check(n,arr,arr_check[i]) == False:
#
#         print('NO')


#2

# n,k = [int(x) for x in input().split()]
# arr = [int(x) for x in input().split()]
# arr_check = [int(x) for x in input().split()]
#
# def binary_check(n,arr,target):
#     left, right = 0, n-1
#     best_index = 0
#     while left <= right:
#         mid = (left+right)//2
#         if arr[mid] == target:
#             return arr[mid]
#         if abs(arr[mid]-target) < abs(arr[best_index]-target) or abs(arr[mid]-target) == abs(arr[best_index]-target) and arr[mid] < arr[best_index]:
#             best_index = mid
#
#         if arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#
#     return arr[best_index]
#
# for i in range(k):
#     print(binary_check(n,arr,arr_check[i]))



#4
# import sys
# import math
#
# C = float(input())
#
# low, high = 0, C  # Устанавливаем границы
# eps = 1e-7  # Гарантируем точность не менее 6 знаков
#
# while high - low > eps:
#     mid = (low + high) / 2
#     f_mid = mid ** 2 + math.sqrt(mid+1)   # Вычисляем f(mid)
#
#     if f_mid <= C:
#         low = mid
#     else:
#         high = mid
#
#
# # Выводим итоговый x
# print(f"{mid}")

#5
# a,b,c,d = [int(x) for x in input().split()]
#
# import sys
# import math
#
# def f(a, b, c, d, x):
#     return a * x**3 + b * x**2 + c * x + d
#
#
# def find_root(a, b, c, d):
#     low, high = -1e6, 1e6
#     eps = 1e-7
#     while high - low > eps:
#         mid = (low + high) / 2  # Вычисляем f(mid)
#         value = f(a,b,c,d,mid)
#         if value== 0:
#             return mid
#         if f(a,b,c,d,low)*value < 0:
#             high = mid
#         else:
#             low = mid
#
# root = find_root(a, b, c, d)
#
# print("{0:.6f}".format(root))

#7
# # Чтение входных данных
# n = int(input())
#
# mass = [int(i) for i in range(1,n+1)]
# def generate_anti_qsort_test(n,mass):
#
#     # Базовый случай: если n <= 1, возвращаем [1]
#     if n <= 1:
#         return [1]
#
#     for i in range(2, n):
#         # Обмениваем mass[i] и mass[i // 2]
#         mass[i], mass[i // 2] = mass[i // 2], mass[i]
#     return mass
#
#
#
#
# # Генерация анти-теста
# anti_test = generate_anti_qsort_test(n,mass)
#
# # Вывод результата
# print(" ".join(map(str, anti_test)))


#9
n = int(input())
p = list(map(int, input().split()))

def search_count(arr):
    max_len = 1
    current_len = 1
    for i in range(1, n):
        if arr[i - 1] == 1 and arr[i] == 0:
            current_len += 1
            if current_len > max_len:
                max_len = current_len
        else:
            current_len = 1
    return max_len

arr = [0] * n
res = [1]  # Изначально массив отсортирован, количество итераций = 1

for i in p:
    arr[i - 1] = 1
    res.append(search_count(arr))

print(" ".join(map(str, res)))