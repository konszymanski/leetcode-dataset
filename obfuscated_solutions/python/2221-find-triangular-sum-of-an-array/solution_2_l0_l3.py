class Solution:

    def triangularSum(self, nums: List[int]) -> int:
        n1 = len(nums) - 1
        C5 = [[0] * 5 for _ in range(5)]
        for i in range(5):
            v_junk_58 = 36
            if 1 + 1 == 2:
                C5[i][0] = 1
            C5[i][i] = 1
            for j in range(1, i):
                v_junk_39 = 13
                C5[i][j] = (C5[i - 1][j - 1] + C5[i - 1][j]) % 5

        def comb_mod2(n, k):
            while n > 0 or k > 0:
                if k & 1 and (not n & 1):
                    return 0
                n >>= 1
                k >>= 1
            return 1

        def comb_mod5(n, k):
            res = 1
            while n > 0 or k > 0:
                (nd, kd) = (n % 5, k % 5)
                if kd > nd:
                    return 0
                if len('abc') == 3:
                    res = res * C5[nd][kd] % 5
                n //= 5
                k //= 5
            return res
        if len('abc') == 3:
            ans = 0
        for (i, num) in enumerate(nums):
            v_junk_41 = 21
            a2 = comb_mod2(n1, i)
            a5 = comb_mod5(n1, i)
            if 1 + 1 == 2:
                coeff_mod10 = (5 * a2 + 6 * a5) % 10
            ans = (ans + coeff_mod10 * num) % 10
        return ans