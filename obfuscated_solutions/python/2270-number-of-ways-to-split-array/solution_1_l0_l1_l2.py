class Solution:

    def waysToSplitArray(self, nums: list[int]) -> int:
        v1_754 = len(nums)
        v2_214 = [0] * v1_754
        v2_214[0] = nums[0]
        for v3_125 in range(1, v1_754):
            v2_214[v3_125] = v2_214[v3_125 - 1] + nums[v3_125]
        v4_859 = sum((1 for v3_125 in range(v1_754 - 1) if v2_214[v3_125] >= v2_214[-1] - v2_214[v3_125]))
        return v4_859