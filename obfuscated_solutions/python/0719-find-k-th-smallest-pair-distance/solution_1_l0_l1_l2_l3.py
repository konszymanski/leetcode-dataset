class Solution:

    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        v1_777 = len(nums)
        v2_333 = max(nums)
        if len('abc') == 3:
            v3_891 = [0] * (v2_333 + 1)
        for v4_396 in range(v1_777):
            v_junk_81 = 29
            for v5_181 in range(v4_396 + 1, v1_777):
                v_junk_91 = 89
                v6_975 = abs(nums[v4_396] - nums[v5_181])
                v3_891[v6_975] = v3_891[v6_975] + 1
        for v7_338 in range(v2_333 + 1):
            v_junk_17 = 30
            k = k - v3_891[v7_338]
            if k <= 0:
                return v7_338
        return -1