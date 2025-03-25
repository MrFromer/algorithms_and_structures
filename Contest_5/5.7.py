from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read().split()
    
    ptr = 0
    n = int(input[ptr])
    ptr += 1
    a = list(map(int, input[ptr:ptr+n]))
    ptr += n
    
    m = int(input[ptr])
    ptr += 1
    b = list(map(int, input[ptr:ptr+m]))
    
    max_len = 0
    min_len = min(n, m)
    
    # Функция для генерации всех возможных ключей подотрезков
    def generate_subarray_keys(arr, length):
        freq = defaultdict(int)
        keys = set()
        
        # Инициализация первого окна
        for i in range(length):
            freq[arr[i]] += 1
        keys.add(tuple(sorted(freq.items())))
        
        # Скользящее окно
        for i in range(1, len(arr) - length + 1):
            # Удаляем предыдущий элемент
            left = arr[i-1]
            freq[left] -= 1
            if freq[left] == 0:
                del freq[left]
            
            # Добавляем новый элемент
            right = arr[i + length - 1]
            freq[right] += 1
            
            # Сохраняем ключ
            keys.add(tuple(sorted(freq.items())))
        
        return keys
    
    # Ищем максимальную длину, начиная с наибольшей возможной
    for L in range(min_len, 0, -1):
        # Генерируем ключи для массива a
        a_keys = generate_subarray_keys(a, L)
        
        # Проверяем массив b на совпадения
        freq = defaultdict(int)
        # Инициализация первого окна
        for i in range(L):
            freq[b[i]] += 1
        if tuple(sorted(freq.items())) in a_keys:
            max_len = L
            break
        
        # Скользящее окно
        found = False
        for i in range(1, m - L + 1):
            # Удаляем предыдущий элемент
            left = b[i-1]
            freq[left] -= 1
            if freq[left] == 0:
                del freq[left]
            
            # Добавляем новый элемент
            right = b[i + L - 1]
            freq[right] += 1
            
            # Проверяем совпадение
            if tuple(sorted(freq.items())) in a_keys:
                max_len = L
                found = True
                break
        
        if found:
            break
    
    print(max_len)

if __name__ == "__main__":
    main()