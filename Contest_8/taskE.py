import sys
input = sys.stdin.read

MOD = 10**9 + 7

class SegmentTree:
    def __init__(self, size):
        self.size = size
        self.max_len = [0] * (2 * size)
        self.cnt = [0] * (2 * size)

    def _combine(self, l_len, l_cnt, r_len, r_cnt):
        if l_len > r_len:
            return l_len, l_cnt
        elif r_len > l_len:
            return r_len, r_cnt
        else:
            return l_len, (l_cnt + r_cnt) % MOD

    def update(self, pos, length, count):
        pos += self.size
        if self.max_len[pos] < length:
            self.max_len[pos] = length
            self.cnt[pos] = count
        elif self.max_len[pos] == length:
            self.cnt[pos] = (self.cnt[pos] + count) % MOD
        while pos > 1:
            pos //= 2
            l_len, l_cnt = self.max_len[2*pos], self.cnt[2*pos]
            r_len, r_cnt = self.max_len[2*pos+1], self.cnt[2*pos+1]
            self.max_len[pos], self.cnt[pos] = self._combine(l_len, l_cnt, r_len, r_cnt)

    def query(self, l, r):
        l += self.size
        r += self.size
        res_len, res_cnt = 0, 0
        while l < r:
            if l % 2 == 1:
                res_len, res_cnt = self._combine(res_len, res_cnt, self.max_len[l], self.cnt[l])
                l += 1
            if r % 2 == 1:
                r -= 1
                res_len, res_cnt = self._combine(res_len, res_cnt, self.max_len[r], self.cnt[r])
            l //= 2
            r //= 2
        return res_len, res_cnt

def main():
    data = input().split()
    n = int(data[0])
    a = list(map(int, data[1:n+1]))

    # Сжатие координат
    unique = sorted(set(a))
    comp = {v: i for i, v in enumerate(unique)}
    a_comp = [comp[x] for x in a]

    size = len(unique)
    st = SegmentTree(size)
    max_lis_len = 0
    total_cnt = 0

    for val in a_comp:
        # ищем максимум среди меньших координат
        if val == 0:
            cur_len, cur_cnt = 0, 0
        else:
            cur_len, cur_cnt = st.query(0, val)
        new_len = cur_len + 1
        new_cnt = cur_cnt if cur_cnt > 0 else 1

        st.update(val, new_len, new_cnt)

        if new_len > max_lis_len:
            max_lis_len = new_len
            total_cnt = new_cnt
        elif new_len == max_lis_len:
            total_cnt = (total_cnt + new_cnt) % MOD

    print(total_cnt)

main()
