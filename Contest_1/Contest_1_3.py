#3
# import sys
# n = int(input())
# def query(x):
#     print(x)
#     sys.stdout.flush()
#     return input()
#
# left, right = 1, n
# while left <= right:
#     mid = (left + right) // 2
#     response = query(mid)
#
#     if response == "<":
#         right = mid - 1
#     else:
#         left = mid + 1
#
# print(f"! {left}")
# sys.stdout.flush()



import sys

n = int(input())
left, right = 1, n


while left <= right:
    mid = (left + right) // 2

    print(mid)
    sys.stdout.flush()

    check_up = input().strip()

    if check_up == '<':
        right = mid - 1
    elif check_up == '>=':
        left = mid + 1

print(f"! {right}")
sys.stdout.flush()
