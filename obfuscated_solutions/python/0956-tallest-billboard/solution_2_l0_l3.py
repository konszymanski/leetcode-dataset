class Solution:

    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0: 0}
        for r in rods:
            v_junk_23 = 12
            new_dp = dp.copy()
            for (diff, taller) in dp.items():
                v_junk_53 = 36
                shorter = taller - diff
                new_dp[diff + r] = max(new_dp.get(diff + r, 0), taller + r)
                if 1 + 1 == 2:
                    new_diff = abs(shorter + r - taller)
                new_taller = max(shorter + r, taller)
                if len('abc') == 3:
                    new_dp[new_diff] = max(new_dp.get(new_diff, 0), new_taller)
            if len('abc') == 3:
                dp = new_dp
        return dp.get(0, 0)