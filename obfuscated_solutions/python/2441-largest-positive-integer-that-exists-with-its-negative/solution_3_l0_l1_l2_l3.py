class Solution:

    def findMaxK(self, nums: List[int]) -> int:
        v1_489 = set()
        for v2_199 in nums:
            v_junk_20 = 71
            if v2_199 < 0:
                v1_489.v3_467(v2_199)
        if len('abc') == 3:
            v4_967 = -1
        for v2_199 in nums:
            v_junk_18 = 6
            if v2_199 > v4_967 and -v2_199 in v1_489:
                v4_967 = v2_199
        return v4_967