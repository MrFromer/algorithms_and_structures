import sys

input = sys.stdin.readline

s = input().split()
N = int(s[0])
K = int(s[1])
Q = int(s[2])

m_list = list(map(int, input().split()))

clasters = []
for count in m_list:
    clast = [[] for _ in range(count)]
    clasters.append(clast)

requests_count = [0] * N

last_access = [[] for _ in range(N)]

def transfer(clast_index):
    if len(last_access[clast_index]) < 2:
        return

    a = last_access[clast_index][-1]
    b = last_access[clast_index][-2]
    if a > b:
        a, b = b, a  

    srv_to_mv = clasters[clast_index][a-1:b]
    clasters[clast_index] = clasters[clast_index][:a-1] + clasters[clast_index][b:]

    target_clast_index = (clast_index + 1) % N
    target_clast = clasters[target_clast_index]

    mid = len(target_clast) // 2
    clasters[target_clast_index] = target_clast[:mid] + srv_to_mv + target_clast[mid:]

    requests_count[clast_index] = 0
    last_access[clast_index] = []


for _ in range(Q):
    line = input().split()
    t = line[0]      
    c = int(line[1]) - 1  
    s = int(line[2]) - 1  
    v = line[3]       

    if len(last_access[c]) == 2:
        last_access[c].pop(0)
    last_access[c].append(s + 1)  

    if t == '+':
        clasters[c][s].append(v)
    elif t == 'p':
        clasters[c][s] = [v + existing for existing in clasters[c][s]]
    elif t == 'c':
        count = 0
        for string in clasters[c][s]:
            if string.startswith(v):
                count += 1
        print(count)

    requests_count[c] += 1
    if requests_count[c] == K:
        transfer(c)
