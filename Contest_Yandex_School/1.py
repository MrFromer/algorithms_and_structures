n = int(input())
a = list(map(int, input().split()))
if n == 0:
    print(0)
    exit()

rev_a = a[::-1]
max_len = 0

base = 10**9 + 7
mod = 10**18 + 3

pow_base = [1] * (n + 1)
for i in range(1, n + 1):
    pow_base[i] = (pow_base[i-1] * base) % mod

def compute_prefix_hash(arr):
    prefix = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        prefix[i+1] = (prefix[i] * base + arr[i]) % mod
    return prefix

a_hash = compute_prefix_hash(a)
rev_a_hash = compute_prefix_hash(rev_a)

def get_hash(prefix, l, r):
    if l > r:
        return 0
    res = (prefix[r+1] - prefix[l] * pow_base[r - l + 1]) % mod
    return res

for i in range(n):
    low = 0
    high = min(i, n-1 - i)
    best_d = 0
    while low <= high:
        mid = (low + high) // 2
        l_p = i - mid
        r_p = i + mid
        rev_l = n - 1 - r_p
        rev_r = n - 1 - l_p
        hash_a_sub = get_hash(a_hash, l_p, r_p)
        hash_rev_sub = get_hash(rev_a_hash, rev_l, rev_r)
        if hash_a_sub == hash_rev_sub:
            best_d = mid
            low = mid + 1
        else:
            high = mid - 1
    current_len = 2 * best_d + 1
    if current_len > max_len:
        max_len = current_len

for i in range(n - 1):
    low = 0
    high = min(i + 1, n - 1 - i)
    best_d = 0
    while low <= high:
        mid = (low + high) // 2
        l_p = i - mid + 1
        r_p = i + mid
        if l_p < 0 or r_p >= n:
            high = mid - 1
            continue
        rev_l = n - 1 - r_p
        rev_r = n - 1 - l_p
        hash_a_sub = get_hash(a_hash, l_p, r_p)
        hash_rev_sub = get_hash(rev_a_hash, rev_l, rev_r)
        if hash_a_sub == hash_rev_sub:
            best_d = mid
            low = mid + 1
        else:
            high = mid - 1
    current_len = 2 * best_d
    if current_len > max_len:
        max_len = current_len

print(max_len if max_len >= 2 else 0)