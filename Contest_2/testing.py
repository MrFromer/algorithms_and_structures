n = int(input())
datas = [int(x) for x in input().replace("\n", " ").split()]


prefix_summ = [0] * (n + 1)
for i in range(n):
    prefix_summ[i + 1] = prefix_summ[i] + datas[i]


left = [-1] * n
stack = []
for i in range(n):
    while stack and datas[stack[-1]] >= datas[i]:
        stack.pop()
    if stack:
        left[i] = stack[-1]
    else:
        left[i] = -1
    stack.append(i)


right = [n] * n
stack = []
for i in range(n - 1, -1, -1):
    while stack and datas[stack[-1]] >= datas[i]:
        stack.pop()
    if stack:
        right[i] = stack[-1]
    else:
        right[i] = n
    stack.append(i)


max_product = 0
for i in range(n):
    l = left[i] + 1
    r = right[i] - 1
    current_sum = prefix_summ[r + 1] - prefix_summ[l]
    current_product = current_sum * datas[i]
    if current_product > max_product:
        max_product = current_product

print(max_product)
