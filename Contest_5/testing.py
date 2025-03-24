MOD1 = 10**18 + 3
BASE1 = 911382629
MOD2 = 10**9 + 7
BASE2 = 35714285

a = input().strip()
b = input().strip()

n = len(b)
m = len(a)

if n == 0 or m < n:
    print(0)
    exit()

max_len = max(2 * n, m)
pow_base1 = [1] * (max_len + 1)
pow_base2 = [1] * (max_len + 1)
for i in range(1, max_len + 1):
    pow_base1[i] = (pow_base1[i-1] * BASE1) % MOD1
    pow_base2[i] = (pow_base2[i-1] * BASE2) % MOD2

def compute_prefix_hashes(s, base, mod):
    prefix = [0] * (len(s) + 1)
    for i in range(len(s)):
        prefix[i+1] = (prefix[i] * base + ord(s[i])) % mod
    return prefix

c = b + b
hash_c1 = compute_prefix_hashes(c, BASE1, MOD1)
hash_c2 = compute_prefix_hashes(c, BASE2, MOD2)

cyclic_hashes = set()
for k in range(n):
    h1 = (hash_c1[k + n] - hash_c1[k] * pow_base1[n]) % MOD1
    h2 = (hash_c2[k + n] - hash_c2[k] * pow_base2[n]) % MOD2
    cyclic_hashes.add((h1, h2))

hash_a1 = compute_prefix_hashes(a, BASE1, MOD1)
hash_a2 = compute_prefix_hashes(a, BASE2, MOD2)

count = 0
for i in range(m - n + 1):
    h1 = (hash_a1[i + n] - hash_a1[i] * pow_base1[n]) % MOD1
    h2 = (hash_a2[i + n] - hash_a2[i] * pow_base2[n]) % MOD2
    if (h1, h2) in cyclic_hashes:
        count += 1

print(count)