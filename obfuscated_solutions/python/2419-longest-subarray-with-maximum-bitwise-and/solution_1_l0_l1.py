class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        v1_754 = v2_214 = v3_125 = 0
        for v4_859 in nums:
            if v1_754  <  v4_859:
                v1_754 = v4_859
                v2_214 = v3_125 = 0
            if v1_754 == v4_859:
                v3_125  +=  1
            else:
                v3_125 = 0
            v2_214 = max(v2_214, v3_125)
        return v2_214
