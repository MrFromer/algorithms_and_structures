import sys
input = sys.stdin.read

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.size = 1
        while self.size < self.n:
            self.size *= 2
        self.tree = [0] * (2 * self.size)
        for i in range(self.n):
            self.tree[self.size + i] = arr[i]
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = max(self.tree[2*i], self.tree[2*i + 1])

    def update(self, i, v):
        pos = self.size + i
        self.tree[pos] = v
        while pos > 1:
            pos //= 2
            self.tree[pos] = max(self.tree[2*pos], self.tree[2*pos + 1])

    def query(self, x, l):
        return self._query(x, l, 1, 0, self.size)

    def _query(self, x, l, node, lx, rx):
        if rx <= l or self.tree[node] < x:
            return -1
        if rx - lx == 1:
            return lx
        mid = (lx + rx) // 2
        res = self._query(x, l, 2*node, lx, mid)
        if res == -1:
            res = self._query(x, l, 2*node+1, mid, rx)
        return res

def main():
    data = input().split()
    n, m = int(data[0]), int(data[1])
    a = list(map(int, data[2:2+n]))
    ops = data[2+n:]

    seg = SegmentTree(a)
    res = []
    i = 0
    while i < len(ops):
        if ops[i] == '1':
            idx = int(ops[i+1])
            val = int(ops[i+2])
            seg.update(idx, val)
            i += 3
        elif ops[i] == '2':
            x = int(ops[i+1])
            l = int(ops[i+2])
            res.append(str(seg.query(x, l)))
            i += 3
    print('\n'.join(res))

main()
