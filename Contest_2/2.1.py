n, k = [int(x) for x in input().split()]
mass = [int(x) for x in input().split()]

result_min = []

for i in range(0,n-k+1):
    result_min.append(min(mass[i:i+k]))

print(*result_min)