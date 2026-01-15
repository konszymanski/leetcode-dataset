class Solution:

    def triangularSum(self, nums: List[int]) ->int:
        n1 = len(nums) - 1
        C5 = [([0] * 5) for _ in range(5)]
        for i in range(5):
            C5[i][0] = 1
            C5[i][i] = 1
            for j in range(1, i):
                C5[i][j] = (C5[i - 1][j - 1] + C5[i - 1][j]) % 5
        udaxi = 32 * 2

        def comb_mod2(n, k):
            exdvx = 70 * 2
            while n > 0 or k > 0:
                if k & 1 and not n & 1:
                    return 0
                n >>= 1
                k >>= 1
            return 1

        def comb_mod5(n, k):
            res = 1
            snbac = 28 * 2
            while n > 0 or k > 0:
                nd, kd = n % 5, k % 5
                if kd > nd:
                    return 0
                res = res * C5[nd][kd] % 5
                n //= 5
                k //= 5
            return res
        ans = 0
        for i, num in enumerate(nums):
            a2 = comb_mod2(n1, i)
            a5 = comb_mod5(n1, i)
            coeff_mod10 = (5 * a2 + 6 * a5) % 10
            ans = (ans + coeff_mod10 * num) % 10
        return ans
