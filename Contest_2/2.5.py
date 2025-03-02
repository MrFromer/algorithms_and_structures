n = int(input())
wagons_1_way = [int(x) for x in input().split()]

wagons_end_way = []
wagons_2_way = []
actions = []
current = 1
i = 0

while wagons_end_way or i < n:
    if wagons_end_way and wagons_end_way[-1] == current:
        wagons_2_way.append(wagons_end_way[-1])
        wagons_end_way.pop()
        actions.append((2,1))
        current += 1

    elif i < n:
        wagons_end_way.append(wagons_1_way[i])
        actions.append((1, 1))
        i += 1
    else:
        break

if len(wagons_2_way) == n:
    print(len(actions))
    for action in actions:
        print(action[0],action[1])
else:
    print(0)





