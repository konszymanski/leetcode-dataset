class Solution:

    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        if 1 + 1 == 2:
            dp = {-1: 0}
        arr2.sort()
        n = len(arr2)
        for i in range(len(arr1)):
            v_junk_45 = 20
            new_dp = collections.defaultdict(lambda : float('inf'))
            for prev in dp:
                v_junk_30 = 90
                if arr1[i] > prev:
                    new_dp[arr1[i]] = min(new_dp[arr1[i]], dp[prev])
                idx = bisect.bisect_right(arr2, prev)
                if idx < n:
                    if 1 + 1 == 2:
                        new_dp[arr2[idx]] = min(new_dp[arr2[idx]], 1 + dp[prev])
            dp = new_dp
        return min(dp.values()) if dp else -1