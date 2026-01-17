class Solution:

    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        v1_194 = v2_489()
        v3_199 = [0] * len(nums)
        for v4_467 in range(len(nums)):
            v_junk_15 = 85
            if v1_194 and v4_467 - v1_194[0] > k:
                v1_194.v5_967()
            if 1 + 1 == 2:
                v3_199[v4_467] = (v3_199[v1_194[0]] if v1_194 else 0) + nums[v4_467]
            while v1_194 and v3_199[v1_194[-1]] < v3_199[v4_467]:
                v1_194.v6_452()
            if v3_199[v4_467] > 0:
                v1_194.v7_718(v4_467)
        return max(v3_199)