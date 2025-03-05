import sys

# Увеличиваем лимит рекурсии для больших деревьев
sys.setrecursionlimit(1 << 25)

def main():
    # Чтение входных данных
    # n — количество вершин в дереве
    # r — корень дерева
    n, r = map(int, sys.stdin.readline().split())

    # Чтение списка детей для каждой вершины
    # children[i] содержит кортеж (left_child, right_child) для вершины i
    # Если left_child или right_child равен -1, это означает, что ребёнок отсутствует
    children = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

    # Функция для проверки, является ли поддерево AVL-деревом
    def is_avl(node, min_val, max_val):
        """
        Рекурсивная функция для проверки, является ли поддерево AVL-деревом.
        :param node: Текущая вершина
        :param min_val: Минимальное допустимое значение для текущей вершины
        :param max_val: Максимальное допустимое значение для текущей вершины
        :return: Кортеж (является ли поддерево AVL-деревом, высота поддерева)
        """
        # Если вершины нет (достигли листа), возвращаем True и высоту 0
        if node == -1:
            return True, 0

        # Проверяем, что значение вершины находится в допустимых границах
        # Для BST: все вершины в левом поддереве должны быть меньше текущей вершины,
        # а все вершины в правом поддереве — больше
        if not (min_val < node < max_val):
            return False, 0

        # Получаем левого и правого ребёнка текущей вершины
        left_child, right_child = children[node]

        # Рекурсивно проверяем левое поддерево
        # Для левого поддерева максимальное значение — текущая вершина (node)
        is_left_avl, left_height = is_avl(left_child, min_val, node)

        # Рекурсивно проверяем правое поддерево
        # Для правого поддерева минимальное значение — текущая вершина (node)
        is_right_avl, right_height = is_avl(right_child, node, max_val)

        # Проверяем сбалансированность поддерева
        # Разница высот левого и правого поддеревьев не должна превышать 1
        if abs(left_height - right_height) > 1:
            return False, 0

        # Если оба поддерева являются AVL-деревьями и сбалансированы,
        # возвращаем True и высоту текущего поддерева
        # Высота поддерева = максимальная высота левого или правого поддерева + 1
        return is_left_avl and is_right_avl, max(left_height, right_height) + 1

    # Запускаем проверку с корня дерева
    # Начальные границы: -бесконечность и +бесконечность
    result, _ = is_avl(r, -float('inf'), float('inf'))

    # Выводим результат
    # Если дерево является AVL-деревом, выводим 1, иначе — 0
    print(1 if result else 0)

if __name__ == "__main__":
    main()