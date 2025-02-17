#1

# n,k = [int(x) for x in input().split()]
# arr = [int(x) for x in input().split()]
# arr_check = [int(x) for x in input().split()]
#
# def binary_check(n,arr,target):
#     left, right = 0, n-1
#     while left <= right:
#         mid = (left+right)//2
#         if arr[mid] == target:
#             return True
#         elif arr[mid] < target:
#             left = mid + 1
#         elif arr[mid] > target:
#             right = mid - 1
#
#     return False
#
# for i in range(k):
#     if binary_check(n,arr,arr_check[i]) == True:
#
#         print('YES')
#     elif binary_check(n,arr,arr_check[i]) == False:
#
#         print('NO')


#2

n,k = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
arr_check = [int(x) for x in input().split()]

def binary_check(n,arr,target):
    left, right = 0, n-1
    best_index = 0
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target:
            return arr[mid]
        if abs(arr[mid]-target) < abs(arr[best_index]-target) or abs(arr[mid]-target) == abs(arr[best_index]-target) and arr[mid] < arr[best_index]:
            best_index = mid

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return arr[best_index]

for i in range(k):
    print(binary_check(n,arr,arr_check[i]))


# 5 5
# 1 3 5 7 9
# 2 4 8 1 6



