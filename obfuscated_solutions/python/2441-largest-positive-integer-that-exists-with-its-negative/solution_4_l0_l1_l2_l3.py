class Solution:

    def findMaxK(self, nums: List[int]) -> int:
        v1_489 = -1
        v2_199 = set()
        for v3_467 in nums:
            v_junk_89 = 47
            v4_967 = abs(v3_467)
            if v4_967 > v1_489 and -v3_467 in v2_199:
                v1_489 = v4_967
            v2_199.v5_452(v3_467)
        return v1_489