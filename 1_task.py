n = int(input())
result = []
min_stack = []
for i in range(n):
    datas = list(map(int, input().split()))
    if datas[0] == 1:
        result.append(datas[1])
        if not min_stack or datas[1] <= min_stack[-1]:
            min_stack.append(datas[1])
    elif datas[0] == 2:
        if result:
            removed_item = result[-1]
            result.pop()
            if removed_item == min_stack[-1]:
                min_stack.pop()
    elif datas[0] == 3:
        if min_stack:
            print(min_stack[-1])
    
