
#УСЛОВИЕ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 7
# 0 0 1 1 1 2
# 6
# 0 1 2 2 2
#        0
#       / \
#      1   2
#     /|\   \
#    3 4 5   6



#СТАРОЕ РЕШЕНИЕ (РАБОТАЕТ НА ПОЛОВИНУ)!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# n = int(input())
# datas = [int(x) for x in input().split()]
# collision_list = [[] for _ in range(n)]

# #поиск глубины для каждой вершины
# def DFS(versina,depth):
#     depths[versina] = depth #заполняю глубину текущей вершины
#     for child in collision_list[versina]: #обходим всех детей в каждом радителе и так рекурсивно до конца дерева
#         DFS(child,depth+1)

# #поиск глубины для каждой вершины
# def DFS_width(versina,depth_w):
#     widths[versina] = depth_w #заполняю глубину текущей вершины
#     for child in collision_list[versina]: #обходим всех детей в каждом радителе и так рекурсивно до конца дерева
#         DFS(child,depth_w+1)

# #строим список смежности за счёт, того, что на вход подаются индексы (текущий элемент), а в datas[i] содержатся значения к какому родителю относится ребёнок (i+1)
# for i in range(n-1):
#     parent = datas[i]
#     child = i + 1
#     collision_list[parent].append(child)
    
# #ищем самую глубокую вершину при помощи алгоритма поиска в глубину (DFS), начиная с корня (вершины "0")
# depths = [0]*n
# DFS(0,0)
# max_depth = max(depths)
# max_depth_index = depths.index(max(depths))


# #ищем ширину, начинаем с самого глубокого элемента и ищем, самый дальний от него
# widths = [0]*n
# DFS_width(max_depth_index,0)
# max_width = max(widths)

# print(max_depth,max_width)
# print(*depths)



#НОВОЕ (ПОЛНОСТЬЮ РАБОЧЕЕ РЕШЕНИЕ)!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

import sys
from collections import deque

# Увеличиваем лимит рекурсии для больших деревьев
sys.setrecursionlimit(1 << 25)

def main():
    # Чтение входных данных
    n = int(sys.stdin.readline())  # Количество вершин в дереве
    parents = list(map(int, sys.stdin.readline().split()))  # Родители для вершин 1..n-1

    # Создаём два представления дерева:
    # 1. Ориентированное дерево (для вычисления глубин вершин)
    # 2. Неориентированный граф (для поиска диаметра дерева)
    directed = [[] for _ in range(n)]  # Ориентированное дерево
    undirected = [[] for _ in range(n)]  # Неориентированный граф

    # Заполняем оба представления дерева
    for i in range(1, n):  # Для каждой вершины i (начиная с 1)
        parent = parents[i - 1]  # Родитель вершины i
        directed[parent].append(i)  # Добавляем ребро parent → i в ориентированное дерево
        undirected[parent].append(i)  # Добавляем ребро parent ↔ i в неориентированный граф
        undirected[i].append(parent)  # Добавляем обратное ребро i ↔ parent

    print(undirected)
    # Функция для вычисления глубин вершин с помощью DFS
    depths = [0] * n  # Массив для хранения глубин вершин

    def dfs(u, d):
        """
        Рекурсивная функция для обхода дерева и вычисления глубин.
        :param u: Текущая вершина
        :param d: Глубина текущей вершины
        """
        depths[u] = d  # Записываем глубину текущей вершины
        for v in directed[u]:  # Рекурсивно обходим всех детей вершины u
            dfs(v, d + 1)

    # Запускаем DFS из корня (вершины 0) с глубиной 0
    dfs(0, 0)
    # Высота дерева — это максимальная глубина среди всех вершин
    height = max(depths)

    # Функция для поиска диаметра дерева с помощью BFS
    def bfs(start):
        """
        Функция для поиска самой удалённой вершины от start и расстояния до неё.
        :param start: Начальная вершина для BFS
        :return: Самая удалённая вершина и расстояние до неё
        """
        visited = [-1] * n  # Массив для хранения расстояний от start до каждой вершины
        q = deque([start])  # Очередь для BFS
        visited[start] = 0  # Расстояние от start до себя равно 0
        max_dist = 0  # Максимальное расстояние
        farthest_node = start  # Самая удалённая вершина

        while q:
            u = q.popleft()  # Извлекаем вершину из очереди
            for v in undirected[u]:  # Перебираем всех соседей вершины u
                if visited[v] == -1:  # Если вершина v ещё не посещена
                    visited[v] = visited[u] + 1  # Обновляем расстояние до v
                    q.append(v)  # Добавляем v в очередь
                    if visited[v] > max_dist:  # Если нашли новую самую удалённую вершину
                        max_dist = visited[v]
                        farthest_node = v

        return farthest_node, max_dist

    # Находим самую удалённую вершину от корня (0)
    u, _ = bfs(0)
    # Находим самую удалённую вершину от u (это и будет диаметр)
    _, diameter = bfs(u)

    # Выводим результаты
    print(height, diameter)  # Высота и диаметр дерева
    print(' '.join(map(str, depths)))  # Глубины всех вершин

if __name__ == "__main__":
    main()



