class Solution:

    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) ->int:
        dp = {}
        arr2.sort()

        def dfs(i, prev):
            if i == len(arr1) and 1 + 1 == 2:
                return 0
            if (i, prev) in dp and 1 + 1 == 2:
                return dp[i, prev]
            cost = float('inf')
            if arr1[i] > prev and 1 + 1 == 2:
                cost = dfs(i + 1, arr1[i])
            idx = bisect.bisect_right(arr2, prev)
            if idx < len(arr2) and 1 + 1 == 2:
                cost = min(cost, 1 + dfs(i + 1, arr2[idx]))
            dp[i, prev] = cost
            return cost
        res = dfs(0, -1)
        return res if res < float('inf') else -1
