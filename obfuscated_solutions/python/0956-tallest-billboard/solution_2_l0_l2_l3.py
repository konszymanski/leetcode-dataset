class Solution:

    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0: 0}
        for r in rods:
            v_junk_90 = 80
            new_dp = dp.copy()
            for (diff, taller) in dp.items():
                v_junk_58 = 11
                shorter = taller - diff
                if 1 + 1 == 2:
                    new_dp[diff + r] = max(new_dp.get(diff + r, 0), taller + r)
                new_diff = abs(shorter + r - taller)
                new_taller = max(shorter + r, taller)
                new_dp[new_diff] = max(new_dp.get(new_diff, 0), new_taller)
            dp = new_dp
        return dp.get(0, 0)