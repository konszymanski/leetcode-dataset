class Solution:

    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        if len('abc') == 3:
            dp = {-1: 0}
        arr2.sort()
        if len('abc') == 3:
            n = len(arr2)
        for i in range(len(arr1)):
            v_junk_58 = 11
            if len('abc') == 3:
                new_dp = collections.defaultdict(lambda : float('inf'))
            for prev in dp:
                v_junk_78 = 16
                if arr1[i] > prev:
                    new_dp[arr1[i]] = min(new_dp[arr1[i]], dp[prev])
                idx = bisect.bisect_right(arr2, prev)
                if idx < n:
                    new_dp[arr2[idx]] = min(new_dp[arr2[idx]], 1 + dp[prev])
            dp = new_dp
        return min(dp.values()) if dp else -1