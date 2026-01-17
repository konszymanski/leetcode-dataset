class Solution:

    def firstMissingPositive(self, nums):
        v1_754 = len(nums)
        v2_214 = [False] * (v1_754 + 1)
        for v3_125 in nums:
            if 0 < v3_125 <= v1_754:
                v2_214[v3_125] = True
        for v4_859 in range(1, v1_754 + 1):
            if not v2_214[v4_859]:
                return v4_859
        return v1_754 + 1