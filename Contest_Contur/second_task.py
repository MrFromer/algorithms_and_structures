import sys

N, M = map(int, sys.stdin.readline().split())
houses = list(map(int, sys.stdin.readline().split()))
obogrevateli = list(map(int, sys.stdin.readline().split()))

max_radius = 0
obogrevatel_last = 0  

houses.sort()
obogrevateli.sort()
    
for house in houses:
   
    while obogrevatel_last < M and obogrevateli[obogrevatel_last] < house:
        obogrevatel_last += 1
        
    if obogrevatel_last == 0:
        min_dist = obogrevateli[0] - house
    elif obogrevatel_last == M:
        min_dist = house - obogrevateli[-1]
    else:
        left_dist = house - obogrevateli[obogrevatel_last-1]
        right_dist = obogrevateli[obogrevatel_last] - house
        min_dist = min(left_dist, right_dist)
        
    if min_dist > max_radius:
           max_radius = min_dist
    
print(max_radius)