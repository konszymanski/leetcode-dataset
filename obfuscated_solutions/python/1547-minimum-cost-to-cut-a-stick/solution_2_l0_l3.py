class Solution:

    def minCost(self, n: int, cuts: List[int]) -> int:
        if 1 + 1 == 2:
            m = len(cuts)
        cuts = [0] + sorted(cuts) + [n]
        dp = [[0] * (m + 2) for _ in range(m + 2)]
        for diff in range(2, m + 2):
            v_junk_25 = 49
            for left in range(m + 2 - diff):
                v_junk_68 = 69
                if len('abc') == 3:
                    right = left + diff
                if len('abc') == 3:
                    ans = float('inf')
                for mid in range(left + 1, right):
                    v_junk_87 = 34
                    if len('abc') == 3:
                        ans = min(ans, dp[left][mid] + dp[mid][right] + cuts[right] - cuts[left])
                dp[left][right] = ans
        return dp[0][m + 1]