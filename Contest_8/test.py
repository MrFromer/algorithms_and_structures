import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    size = 1
    while size < n:
        size <<= 1
    tree = [-1] * (2 * size)
    
    # Построение дерева
    for i in range(n):
        tree[size + i] = arr[i]
    for i in range(size - 1, 0, -1):
        tree[i] = max(tree[2 * i], tree[2 * i + 1])
    
    # Обновление элемента
    def update(pos, val):
        pos += size
        tree[pos] = val
        pos >>= 1
        while pos >= 1:
            new_val = max(tree[2 * pos], tree[2 * pos + 1])
            if tree[pos] == new_val:
                break
            tree[pos] = new_val
            pos >>= 1
    
    # Поиск первого элемента > x после l
    def query(x, l):
        res = -1
        # Начинаем с правого конца
        left = l + 1
        right = n - 1
        if left > right:
            return -1
        
        left += size
        right += size
        candidates = []
        
        while left <= right:
            if left % 2 == 1:
                candidates.append(left)
                left += 1
            if right % 2 == 0:
                candidates.append(right)
                right -= 1
            left >>= 1
            right >>= 1
        
        for node in candidates:
            current = node
            while current < size:
                if tree[2 * current] > x:
                    current = 2 * current
                else:
                    current = 2 * current + 1
            idx = current - size
            if idx <= n - 1 and tree[current] > x:
                if res == -1 or idx < res:
                    res = idx
        return res if res != -1 else -1
    
    for _ in range(m):
        parts = list(map(int, input().split()))
        if parts[0] == 1:
            i, v = parts[1], parts[2]
            update(i, v)
        else:
            x, l = parts[1], parts[2]
            print(query(x, l))

if __name__ == "__main__":
    main()