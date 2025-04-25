import sys
input = sys.stdin.readline  # Оптимизация ввода для больших объемов данных
n = input().split()

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

stroim_derevo(0, 0, n - 1)

def find_increase(v, tl, tr, k):

    if tl == tr:
        return tl

    middle = (tl + tr) // 2
    left_child = trees[v*2+1]

    if left_child > k:
        return find_one(v * 2 + 1, tl, middle, k)
    else:
        return find_one(v * 2 + 2, middle + 1, tr, k-left_child)
   


