class Solution:

    def minCost(self, n: int, cuts: List[int]) ->int:
        m = len(cuts)
        cuts = [0] + sorted(cuts) + [n]
        dp = [([0] * (m + 2)) for _ in range(m + 2)]
        diff = 2
        while diff < m + 2:
            for left in range(m + 2 - diff):
                right = left + diff
                ans = float('inf')
                for mid in range(left + 1, right):
                    ans = min(ans, dp[left][mid] + dp[mid][right] + cuts[
                        right] - cuts[left])
                dp[left][right] = ans
            diff += 1
        return dp[0][m + 1]
