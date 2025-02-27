def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    queries = []
    index = 1
    for _ in range(t):
        n = int(data[index])
        m = int(data[index + 1])
        queries.append((n, m))
        index += 2
    
    results = []
    for n, m in queries:
        S = n * m * (n * m + 1) // 2
        half = S // 2
        
        # Поиск вертикального разреза
        best_diff = float('inf')
        best_x = 0
        for x in range(1, m + 1):
            S_left = n * x * (x + 1) // 2 + n * (n - 1) * m * x // 2
            diff = abs(S_left - half)
            if diff < best_diff:
                best_diff = diff
                best_x = x
        
        # Поиск горизонтального разреза
        best_k = 0
        for k in range(1, n + 1):
            S_top = k * m * (k * m + 1) // 2
            diff = abs(S_top - half)
            if diff < best_diff:
                best_diff = diff
                best_k = k
        
        # Выбор разреза
        if best_k == 0:
            results.append(f"V {best_x}")
        else:
            results.append(f"H {best_k}")
    
    # Вывод результатов
    print("\n".join(results))

if __name__ == "__main__":
    main()