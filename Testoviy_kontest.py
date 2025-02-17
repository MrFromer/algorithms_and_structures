# n,k = [int(x) for x in input().split()]
# arr = sorted([int(x) for x in input().split()])
#
#
# def count_less_x(arr, x):
#     left, right = 0, len(arr)
#     while left < right:
#         mid = (left + right) // 2
#         if arr[mid] <= x:
#             left = mid + 1
#         else:
#             right = mid
#     return left
#
# def poisk_x(arr,k):
#     left, right = 0, 10**9
#
#     while left < right:
#         mid = (left + right)//2
#         if count_less_x(arr, mid) <= k:
#             left = mid
#         else:
#             right = mid - 1
#
#     if count_less_x(arr, left) == k:
#         return left-1
#     return -1
#
#
#
# print(poisk_x(arr,k))


import sys
import bisect

def find_kth_number(arr, k):
    left, right = 1, 10**9
    while left < right:
        mid = (left + right + 1) // 2
        if bisect.bisect_right(arr, mid) <= k:
            left = mid
        else:
            right = mid - 1

    return left if bisect.bisect_right(arr, left) == k else -1

def main():
    n, k = map(int, sys.stdin.readline().split())
    arr = sorted(map(int, sys.stdin.readline().split()))
    print(find_kth_number(arr, k))

if __name__ == "__main__":
    main()

