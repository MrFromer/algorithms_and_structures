import sys
sys.setrecursionlimit(200000)

n, m = [int(x) for x in input().split()]

spisok_smezh = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = [int(x) for x in input().split()]
    spisok_smezh[a].append(b)
    spisok_smezh[b].append(a)

#print(spisok_smezh)

components = []
visited_vertexs = [False]*(n+1)

def DFS(vertex, component):
    visited_vertexs[vertex] = True
    component.append(vertex)
    for children in spisok_smezh[vertex]:
        if not visited_vertexs[children]:
            DFS(children,component)


for vertex in range(1,n+1):
    if not visited_vertexs[vertex]:
        component = []
        DFS(vertex,component)
        components.append(sorted(component))

print(len(components))

for i in range(len(components)):
    print(len(components[i]))
    print(*components[i])