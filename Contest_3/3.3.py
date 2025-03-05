# Считываем количество вершин в дереве
n = int(input())

# Считываем массив предков для каждой вершины (начиная с вершины 1)
# Например, для входных данных "0 0 1 1":
# Вершина 1 имеет предка 0, вершина 2 имеет предка 0, вершина 3 имеет предка 1, вершина 4 имеет предка 1
datas = [int(x) for x in input().split()]

# Считываем количество запросов
m = int(input())

# Создаем список для хранения пар вершин, для которых нужно найти LCA
pares = []
for i in range(m):
    # Считываем пару вершин и добавляем её в список
    pares.append([int(x) for x in input().split()])

# Добавляем корень дерева (вершину 0) в массив предков
# Теперь datas = [-1, 0, 0, 1, 1], где datas[0] = -1 (корень не имеет предка)
datas.insert(0, -1)

# Функция для поиска пути от вершины u до корня
def search_path(u, datas):
    path = []  # Список для хранения пути
    # Поднимаемся от вершины u до корня
    while u != -1:
        path.append(u)  # Добавляем текущую вершину в путь
        u = datas[u]    # Переходим к предку
    return path

# Функция для нахождения LCA двух вершин
def check_in(pare, datas):
    # Находим путь от первой вершины до корня
    path_1 = search_path(pare[0], datas)
    # Находим путь от второй вершины до корня
    path_2 = search_path(pare[1], datas)
    
    # Ищем последнюю общую вершину в двух путях
    for versina_1 in path_1:
        for versina_2 in path_2:
            if versina_1 == versina_2:
                return versina_1  # Возвращаем LCA

# Обрабатываем каждый запрос
for pare in pares:
    # Выводим LCA для текущей пары вершин
    print(check_in(pare, datas))


# Пример входных данных:
# 5
# 0 0 1 1
# 3
# 3 4
# 3 1
# 2 4
# Визуализация дерева:
#      0
#     / \
#    1   2
#   / \
#  3   4
