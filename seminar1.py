#11 Pref summ
pref_sum = []
spisok = [int(x) for x in input().split()]
for i in range(0,len(spisok)):
    pref_sum[i+1] = pref_sum[i] + spisok[i]

#ищем число, которое будет больше суммы чисел (преф сумм.) через бинарный поиск
l = 0
r = len(spisok) + 2
S = int(input())
# pref_sum[l] <= S; pref[r] > S
while(r-l>1):
    mid = (l+r)/2
    if pref_sum[mid] <= S:
        l = mid
    else:
        r = mid

