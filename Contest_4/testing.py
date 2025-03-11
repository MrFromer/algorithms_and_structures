import sys

# Чтение данных
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

# Префиксные суммы и префиксные XOR
prefix_sum = [0] * (n + 1)
prefix_xor = [0] * (n + 1)

for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]
    prefix_xor[i] = prefix_xor[i - 1] ^ arr[i - 1]

# Обработка запросов
output = []
for _ in range(m):
    q, l, r = map(int, sys.stdin.readline().split())
    if q == 1:  # Запрос суммы
        result = prefix_sum[r] - prefix_sum[l - 1]
    else:  # Запрос XOR
        result = prefix_xor[r] ^ prefix_xor[l - 1]
    output.append(str(result))

# Вывод всех результатов
print('\n'.join(output))
