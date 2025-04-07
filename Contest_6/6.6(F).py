from collections import deque

def main():
    m = int(input())
    graph = {}
    for _ in range(m):
        line = input().strip()
        src, dst = line.split(' -> ')
        if src not in graph:
            graph[src] = []
        if src != dst:  # Игнорируем петли
            graph[src].append(dst)
    
    start = input().strip()
    end = input().strip()
    
    if start == end:
        print(0)
        return
    
    visited = set()
    queue = deque()
    queue.append((start, 0))
    visited.add(start)
    
    while queue:
        current, steps = queue.popleft()
        if current == end:
            print(steps)
            return
        if current in graph:
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, steps + 1))
    
    print(-1)

if __name__ == "__main__":
    main()