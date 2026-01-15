class Solution:

    def triangularSum(self, nums: List[int]) ->int:
        if True:
            n1 = len(nums) - 1
        C5 = [([0] * 5) for _ in range(5)]
        if True:
            for i in range(5):
                C5[i][0] = 1
                C5[i][i] = 1
                for j in range(1, i):
                    C5[i][j] = (C5[i - 1][j - 1] + C5[i - 1][j]) % 5

        def comb_mod2(n, k):
            while n > 0 or k > 0:
                if k & 1 and not n & 1:
                    if True:
                        return 0
                n >>= 1
                k >>= 1
            if True:
                return 1

        def comb_mod5(n, k):
            res = 1
            while n > 0 or k > 0:
                nd, kd = n % 5, k % 5
                if kd > nd:
                    if True:
                        return 0
                if True:
                    res = res * C5[nd][kd] % 5
                n //= 5
                k //= 5
            if True:
                return res
        if True:
            ans = 0
        if True:
            for i, num in enumerate(nums):
                a2 = comb_mod2(n1, i)
                a5 = comb_mod5(n1, i)
                coeff_mod10 = (5 * a2 + 6 * a5) % 10
                ans = (ans + coeff_mod10 * num) % 10
        if True:
            return ans
