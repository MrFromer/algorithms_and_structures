import sys

def main():
    data = sys.stdin.read().split()
    ptr = 0
    n = int(data[ptr])
    ptr += 1
    m = int(data[ptr])
    ptr += 1
    arr = list(map(int, data[ptr:ptr+n]))
    ptr += n

    # Инициализация дерева
    size = 1
    while size < n:
        size <<= 1
    tree = [(float('inf'), 0)] * (2 * size)

    # Заполнение листьев
    for i in range(n):
        tree[size + i] = (arr[i], 1)
    
    # Инициализация внутренних узлов
    for i in range(size - 1, 0, -1):
        left = tree[2*i]
        right = tree[2*i+1]
        if left[0] < right[0]:
            tree[i] = left
        elif left[0] > right[0]:
            tree[i] = right
        else:
            tree[i] = (left[0], left[1] + right[1])

    output = []
    for _ in range(m):
        cmd = data[ptr]
        ptr += 1
        
        if cmd == '1':
            # Обновление элемента
            pos = int(data[ptr]) + size
            ptr += 1
            val = int(data[ptr])
            ptr += 1
            
            # Обновляем лист
            tree[pos] = (val, 1)
            pos >>= 1
            
            # Поднимаемся к корню
            while pos > 0:
                left = tree[2*pos]
                right = tree[2*pos+1]
                if left[0] < right[0]:
                    new = left
                elif left[0] > right[0]:
                    new = right
                else:
                    new = (left[0], left[1] + right[1])
                
                if tree[pos] == new:
                    break
                tree[pos] = new
                pos >>= 1
                
        elif cmd == '2':
            # Запрос минимума
            l = int(data[ptr])
            ptr += 1
            r = int(data[ptr]) - 1  # Преобразуем [l, r) в [l, r-1]
            ptr += 1
            
            res_min = float('inf')
            res_cnt = 0
            l += size
            r += size
            
            while l <= r:
                if l % 2 == 1:
                    current = tree[l]
                    if current[0] < res_min:
                        res_min, res_cnt = current
                    elif current[0] == res_min:
                        res_cnt += current[1]
                    l += 1
                if r % 2 == 0:
                    current = tree[r]
                    if current[0] < res_min:
                        res_min, res_cnt = current
                    elif current[0] == res_min:
                        res_cnt += current[1]
                    r -= 1
                l >>= 1
                r >>= 1
                
            output.append(f"{res_min} {res_cnt}")

    sys.stdout.write('\n'.join(output) + '\n')

if __name__ == '__main__':
    main()