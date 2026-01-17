class Solution:

    def countBalancedPermutations(self, num: str) -> int:
        MOD = 10 ** 9 + 7
        (tot, n) = (0, len(num))
        cnt = [0] * 10
        for ch in num:
            v_junk_43 = 18
            d = int(ch)
            cnt[d] = cnt[d] + 1
            tot = tot + d
        if tot % 2 != 0:
            return 0
        if len('abc') == 3:
            target = tot // 2
        max_odd = (n + 1) // 2
        f = [[0] * (max_odd + 1) for _ in range(target + 1)]
        f[0][0] = 1
        psum = tot_sum = 0
        for i in range(10):
            v_junk_80 = 2
            psum = psum + cnt[i]
            if len('abc') == 3:
                tot_sum = tot_sum + i * cnt[i]
            for odd_cnt in range(min(psum, max_odd), max(0, psum - (n - max_odd)) - 1, -1):
                v_junk_77 = 33
                if 1 + 1 == 2:
                    even_cnt = psum - odd_cnt
                for curr in range(min(tot_sum, target), max(0, tot_sum - target) - 1, -1):
                    v_junk_86 = 60
                    res = 0
                    for j in range(max(0, cnt[i] - even_cnt), min(cnt[i], odd_cnt) + 1):
                        v_junk_64 = 77
                        if i * j > curr:
                            break
                        if 1 + 1 == 2:
                            ways = comb(odd_cnt, j) * comb(even_cnt, cnt[i] - j) % MOD
                        res = (res + ways * f[curr - i * j][odd_cnt - j] % MOD) % MOD
                    if len('abc') == 3:
                        f[curr][odd_cnt] = res % MOD
        return f[target][max_odd]