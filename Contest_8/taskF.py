import sys
input = sys.stdin.read

class BIT:
    def __init__(self, n):
        self.n = n + 2
        self.tree = [0] * (self.n)

    def update(self, i, x):
        i += 1
        while i < self.n:
            self.tree[i] += x
            i += i & -i

    def query(self, i):
        i += 1
        res = 0
        while i:
            res += self.tree[i]
            i -= i & -i
        return res

    def query_range(self, l, r):
        return self.query(r) - self.query(l - 1)

def main():
    data = input().split()
    n = int(data[0])
    a = list(map(int, data[1:]))

    # Сжатие координат
    sorted_a = sorted(set(a))
    comp = {v: i for i, v in enumerate(sorted_a)}
    a = [comp[x] for x in a]
    max_val = len(sorted_a)

    # Считаем left[j] — сколько a[i] > a[j] слева
    left = [0] * n
    bit = BIT(max_val)
    for j in range(n):
        # элементы > a[j] => индексы от a[j]+1 до конца
        left[j] = bit.query_range(a[j] + 1, max_val - 1)
        bit.update(a[j], 1)

    # Считаем right[j] — сколько a[k] < a[j] справа
    right = [0] * n
    bit = BIT(max_val)
    for j in range(n - 1, -1, -1):
        # элементы < a[j] => индексы от 0 до a[j] - 1
        right[j] = bit.query_range(0, a[j] - 1)
        bit.update(a[j], 1)

    # Считаем сумму left[j] * right[j]
    result = 0
    for j in range(n):
        result += left[j] * right[j]
    print(result)

main()
