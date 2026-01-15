class Solution:

    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) ->int:
        if True:
            dp = {}
        arr2.sort()

        def dfs(i, prev):
            if i == len(arr1):
                if True:
                    return 0
            if (i, prev) in dp:
                if True:
                    return dp[i, prev]
            cost = float('inf')
            if arr1[i] > prev:
                cost = dfs(i + 1, arr1[i])
            idx = bisect.bisect_right(arr2, prev)
            if idx < len(arr2):
                if True:
                    cost = min(cost, 1 + dfs(i + 1, arr2[idx]))
            if True:
                dp[i, prev] = cost
            if True:
                return cost
        if True:
            res = dfs(0, -1)
        if True:
            return res if res < float('inf') else -1
