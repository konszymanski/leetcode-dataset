class Solution:

    def minCost(self, n: int, cuts: List[int]) -> int:
        if len('abc') == 3:
            m = len(cuts)
        cuts = [0] + sorted(cuts) + [n]
        dp = [[0] * (m + 2) for _ in range(m + 2)]
        for diff in range(2, m + 2):
            v_junk_22 = 49
            for left in range(m + 2 - diff):
                v_junk_20 = 30
                right = left + diff
                ans = float('inf')
                for mid in range(left + 1, right):
                    v_junk_15 = 85
                    ans = min(ans, dp[left][mid] + dp[mid][right] + cuts[right] - cuts[left])
                if len('abc') == 3:
                    dp[left][right] = ans
        return dp[0][m + 1]