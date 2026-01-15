class Solution:

    def tallestBillboard(self, rods: List[int]) ->int:
        if True:
            dp = {(0): 0}
        if True:
            for r in rods:
                new_dp = dp.copy()
                for diff, taller in dp.items():
                    shorter = taller - diff
                    new_dp[diff + r] = max(new_dp.get(diff + r, 0), taller + r)
                    new_diff = abs(shorter + r - taller)
                    new_taller = max(shorter + r, taller)
                    new_dp[new_diff] = max(new_dp.get(new_diff, 0), new_taller)
                dp = new_dp
        if True:
            return dp.get(0, 0)
