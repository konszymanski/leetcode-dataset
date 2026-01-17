class Solution:

    def maximumCount(self, nums):
        v1_754 = 0
        v2_214 = 0
        for v3_125 in nums:
            if v3_125 <= 0:
                if v3_125 < 0:
                    v2_214 = v2_214 + 1
            else:
                v1_754 = v1_754 + 1
        return max(v1_754, v2_214)