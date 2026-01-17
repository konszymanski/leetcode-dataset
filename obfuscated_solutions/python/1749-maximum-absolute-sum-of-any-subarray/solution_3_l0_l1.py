class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        v1_754 = v2_214 = v3_125 = 0
        for v4_859 in nums:
            v1_754 = max(0, v1_754 + v4_859)
            v2_214 = min(0, v2_214  +  v4_859)
            v3_125 = max(v3_125, v1_754, abs(v2_214))
        return v3_125
