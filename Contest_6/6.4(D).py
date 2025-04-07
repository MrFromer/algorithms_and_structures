#Мой не оптимальный код через сумму координат

# n = int(input())
# x1, y1 = [int(x) for x in input().split()]
# x2, y2 = [int(x) for x in input().split()]
# x1, y1 = x1 + 2, y1 + 2
# x2, y2 = x2 + 2, y2 + 2

# matrixx = [[-1]*(n+4) for _ in range(n+4)]

# for i in range(2,n+2):
#     for j in range(2,n+2):
#         matrixx[i][j] = i-1 + j-1

# print(matrixx)

# count = 0
# aim = matrixx[x2][y2]

# def possible_knight_moves(i, j):
#     moves = []
#     # Все 8 возможных смещений для хода коня
#     deltas = [
#         (2, 1), (2, -1),
#         (-2, 1), (-2, -1),
#         (1, 2), (1, -2),
#         (-1, 2), (-1, -2)
#     ]
#     for di, dj in deltas:
#         new_i, new_j = i + di, j + dj
#         moves.append((new_i, new_j))
    
#     return moves

# for i in range(x1,n+2):
#     for j in range(y1,n+2):
#         p1 = i + 2 + j + 1
#         p2 = i + 2 + j - 1
#         p3 = i - 2 + j + 1
#         p4 = i - 2 + j - 1
#         p5 = i + 1 + j + 2
#         p6 = i + 1 + j - 2
#         p7 = i - 1 + j + 2
#         p8 = i - 1 + j - 2
#         path = min(aim - p1, aim - p2, aim - p3, aim - p4, aim - p5, aim - p6, aim - p7, aim - p8)



#Поиск кратчайшего пути при помощи BFS

n = int(input())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

# Возможные ходы коня (8 направлений)
moves = [
    (2, 1), (2, -1),
    (-2, 1), (-2, -1),
    (1, 2), (1, -2),
    (-1, 2), (-1, -2)
]



def BFS_knight(x1,y1,x2,y2):
    visited = [[False for _ in range(n+1)] for _ in range(n+1)]
    queue = []
    queue.append((x1,y1,0, [(x1,y1)]))
    visited[x1][y1] = True

    while queue:
        x, y, steps, path = queue.pop(0)

        if x == x2 and y == y2:
            return steps, path

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 1 <= nx <= n and 1 <= ny <= n and not visited[nx][ny]:
                visited[nx][ny] = True
                new_path = path.copy()
                new_path.append((nx,ny))
                queue.append((nx,ny,steps+1, new_path))
                
    return -1, []

steps, path = BFS_knight(x1,y1,x2,y2)
print(steps)
if steps != -1:
    for point in path:
        print(*point)