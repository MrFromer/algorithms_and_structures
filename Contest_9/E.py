import sys
input = sys.stdin.readline
from collections import defaultdict
from bisect import bisect_left

n = int(input())

horiz = defaultdict(list)  # y -> list of (x1, x2)
vert = defaultdict(list)   # x -> list of (y1, y2)
segments = []

ys = set()

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 > x2: x1, x2 = x2, x1
    if y1 > y2: y1, y2 = y2, y1
    if y1 == y2:
        horiz[y1].append((x1, x2))
        ys.add(y1)
    else:
        vert[x1].append((y1, y2))
        ys.add(y1)
        ys.add(y2)
    segments.append((x1, y1, x2, y2))

# --- Сжимаем координаты по y ---
ys = sorted(ys)
y_id = {v: i for i, v in enumerate(ys)}
m = len(ys)

class Fenwick:
    def __init__(self, n):
        self.t = [0] * (n+2)

    def add(self, i, v):
        i += 1
        while i < len(self.t):
            self.t[i] += v
            i += i & -i

    def query(self, i):
        i += 1
        res = 0
        while i > 0:
            res += self.t[i]
            i -= i & -i
        return res

    def range_query(self, l, r):
        return self.query(r) - self.query(l-1)

# --- Подсчёт уникальных клеток по объединённым отрезкам ---

def merge(intervals):
    if not intervals:
        return []
    intervals.sort()
    res = []
    cur_l, cur_r = intervals[0]
    for l, r in intervals[1:]:
        if l <= cur_r + 1:
            cur_r = max(cur_r, r)
        else:
            res.append((cur_l, cur_r))
            cur_l, cur_r = l, r
    res.append((cur_l, cur_r))
    return res

total = 0
events = []

# Считаем длину всех горизонтальных отрезков + генерируем события для sweep line
for y in horiz:
    merged = merge(horiz[y])
    for x1, x2 in merged:
        total += x2 - x1 + 1
        events.append((x1, 0, y))  # начало
        events.append((x2 + 1, 1, y))  # конец

# Считаем длину всех вертикальных отрезков
for x in vert:
    merged = merge(vert[x])
    for y1, y2 in merged:
        total += y2 - y1 + 1
        events.append((x, 2, y1, y2))  # запрос на пересечение

# --- Sweep line по x, Fenwick по y ---
events.sort()
ft = Fenwick(m)

for ev in events:
    if ev[1] == 0:
        _, _, y = ev
        ft.add(y_id[y], 1)
    elif ev[1] == 1:
        _, _, y = ev
        ft.add(y_id[y], -1)
    else:
        _, _, y1, y2 = ev
        l = bisect_left(ys, y1)
        r = bisect_left(ys, y2)
        total -= ft.range_query(l, r)

print(total)
