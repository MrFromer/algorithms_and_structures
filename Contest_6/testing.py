from heapq import heappush, heappop

def find_min_digit_sum(K):
    min_sum = [float('inf')] * K
    heap = []
    
    # Инициализация: начинаем с цифр 1-9
    for digit in range(1, 10):
        rem = digit % K
        if digit < min_sum[rem]:
            min_sum[rem] = digit
            heappush(heap, (digit, rem))
    
    while heap:
        s, rem = heappop(heap)
        
        # Ранний выход при нахождении решения
        if rem == 0:
            return s
        
        # Пропускаем устаревшие состояния
        if s > min_sum[rem]:
            continue
        
        # Генерируем новые состояния
        for d in range(0, 10):
            new_rem = (rem * 10 + d) % K
            new_s = s + d
            
            if new_s < min_sum[new_rem]:
                min_sum[new_rem] = new_s
                heappush(heap, (new_s, new_rem))
    
    return min_sum[0]

K = int(input())
print(find_min_digit_sum(K))