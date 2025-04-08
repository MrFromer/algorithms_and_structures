import sys
from collections import deque


n, m, k = map(int, sys.stdin.readline().split())
edges = []
max_s = 0
    
for _ in range(m):
    u, v, s = map(int, sys.stdin.readline().split())
    edges.append((s, u-1, v-1))
    if s > max_s:
         max_s = s
    
edges.sort()  
    
def is_possible(level):
        
    adj = [[] for _ in range(n)]
    in_degree = [0] * n
        
        
    for s, u, v in edges:
        if s > level:
            continue
        adj[u].append(v)
        in_degree[v] += 1
        
        
    q = deque()
    for i in range(n):
        if in_degree[i] == 0:
            q.append(i)
        
        topo_order = []
    while q:
        u = q.popleft()
        topo_order.append(u)
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)
        
        
    if len(topo_order) < n:
        return True
        
        
    max_path = [0] * n
    max_len = 0
    for u in topo_order:
        for v in adj[u]:
            if max_path[v] < max_path[u] + 1:
                max_path[v] = max_path[u] + 1
                if max_path[v] >= k:
                    return True
    return False
    
    
left, right = 0, max_s
answer = -1
while left <= right:
    mid = (left + right) // 2
    if is_possible(mid):
        answer = mid
        right = mid - 1
    else:
        left = mid + 1
    
print(answer)

