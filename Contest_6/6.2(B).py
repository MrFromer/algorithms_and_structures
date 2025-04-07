import sys
sys.setrecursionlimit(200000)

n, m = [int(x) for x in input().split()]

spisok_smezh = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = [int(x) for x in input().split()]
    spisok_smezh[a].append(b)
    

visited_vertexs = [0]*(n+1)
cycle = False

def DFS(v):
    global cycle
    visited_vertexs[v] = 1
    for children in spisok_smezh[v]:
        if visited_vertexs[children] == 0:
            DFS(children)
        elif visited_vertexs[children] == 1:
            cycle = True
            return True
    visited_vertexs[v] = 2
        


for v in range(1,n+1):
    if visited_vertexs[v] == 0:
        DFS(v)

if cycle:
    print(1)
else:
    print(0)


