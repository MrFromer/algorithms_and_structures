import sys
input = sys.stdin.readline  # Оптимизация ввода для больших объемов данных
n, m = map(int, input().split())

logs_moments = list(map(int, input().split()))

trees = [0] * (4 * n)

def stroim_derevo(v, tl, tr):
    if tl == tr:
        trees[v] = logs_moments[tl]
    else:
        middle = (tl + tr) // 2

        stroim_derevo(v * 2 + 1, tl, middle)

        stroim_derevo(v * 2 + 2, middle + 1, tr)

        trees[v] = trees[v * 2 + 1] + trees[v * 2 + 2]


def change_derevo(v, tl, tr, pos):
    if tl == tr:
        trees[v] = 1 - trees[v]

    else:
        middle = (tl + tr) // 2
        if pos <= middle:
            change_derevo(v * 2 + 1, tl, middle, pos)
        else:
            change_derevo(v * 2 + 2, middle + 1, tr, pos)

        trees[v] = trees[v * 2 + 1] + trees[v * 2 + 2]


def find_one(v, tl, tr, k):

    if tl == tr:
        return tl

    middle = (tl + tr) // 2
    left_child = trees[v*2+1]

    if left_child > k:
        return find_one(v * 2 + 1, tl, middle, k)
    else:
        return find_one(v * 2 + 2, middle + 1, tr, k-left_child)
   

# Построили дерево на основе изначального массива логов
stroim_derevo(0, 0, n - 1)

for _ in range(m):
    line = list(map(int, input().split()))
    type = line[0]

    if type == 1:
        # Запрос на изменение: "1 i v" — изменить i-й лог на значение v
        i = line[1]
        change_derevo(0, 0, n - 1, i)

    elif type == 2:
        k = line[1]
        print(find_one(0, 0, n - 1, k))  