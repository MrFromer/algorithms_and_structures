n, m = map(int, input().split())

# Инициализация матрицы DP
dp = [[0] * m for _ in range(n)]
dp[0][0] = 1  # Начальная позиция

# Все возможные ходы коня (8 направлений)
moves = [
    (2, 1), (1, 2),
    (-1, 2), (-2, 1),
    (-2, -1), (-1, -2),
    (1, -2), (2, -1)
]

# Перебор по диагоналям (i + j = const)
for s in range(1, n + m - 1):
    for i in range(max(0, s - m + 1), min(n, s + 1)):
        j = s - i
        # Проверяем все возможные ходы коня
        for di, dj in moves:
            pi, pj = i - di, j - dj
            if 0 <= pi < n and 0 <= pj < m:
                dp[i][j] += dp[pi][pj]

print(dp[n-1][m-1])