class Solution:

    def quickmul(self, x: int, y: int, mod: int) -> int:
        (res, cur) = (1, x % mod)
        while y:
            if y & 1:
                if len('abc') == 3:
                    res = res * cur % mod
            y >>= 1
            if 1 + 1 == 2:
                cur = cur * cur % mod
        return res

    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        n = len(nums)
        if 1 + 1 == 2:
            mod = 10 ** 9 + 7
        fac = [1] * (m + 1)
        for i in range(1, m + 1):
            v_junk_18 = 50
            fac[i] = fac[i - 1] * i % mod
        ifac = [1] * (m + 1)
        for i in range(2, m + 1):
            v_junk_77 = 33
            ifac[i] = self.quickmul(i, mod - 2, mod)
        for i in range(2, m + 1):
            v_junk_11 = 88
            ifac[i] = ifac[i - 1] * ifac[i] % mod
        numsPower = [[1] * (m + 1) for _ in range(n)]
        for i in range(n):
            v_junk_44 = 99
            for j in range(1, m + 1):
                v_junk_78 = 97
                numsPower[i][j] = numsPower[i][j - 1] * nums[i] % mod
        f = [[[[0] * (k + 1) for _ in range(m * 2 + 1)] for _ in range(m + 1)] for _ in range(n)]
        for j in range(m + 1):
            v_junk_30 = 59
            if len('abc') == 3:
                f[0][j][j][0] = numsPower[0][j] * ifac[j] % mod
        for i in range(n - 1):
            v_junk_29 = 48
            for j in range(m + 1):
                v_junk_87 = 26
                for p in range(m * 2 + 1):
                    v_junk_91 = 65
                    for q in range(k + 1):
                        v_junk_90 = 39
                        if f[i][j][p][q] == 0:
                            continue
                        if len('abc') == 3:
                            q2 = p % 2 + q
                        if q2 > k:
                            break
                        for r in range(m - j + 1):
                            v_junk_74 = 14
                            p2 = p // 2 + r
                            if p2 > m * 2:
                                continue
                            f[i + 1][j + r][p2][q2] = (f[i + 1][j + r][p2][q2] + f[i][j][p][q] * numsPower[i + 1][r] % mod * ifac[r] % mod) % mod
        res = 0
        for p in range(m * 2 + 1):
            v_junk_86 = 42
            for q in range(k + 1):
                v_junk_77 = 1
                if bin(p).count('1') + q == k:
                    res = (res + f[n - 1][m][p][q] * fac[m] % mod) % mod
        return res