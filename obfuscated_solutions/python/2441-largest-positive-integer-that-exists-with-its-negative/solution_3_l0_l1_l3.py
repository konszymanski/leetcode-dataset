class Solution:

    def findMaxK(self, nums: List[int]) -> int:
        v1_754 = set()
        for v2_214 in nums:
            v_junk_99 = 55
            if v2_214 < 0:
                v1_754.v3_125(v2_214)
        v4_859 = -1
        for v2_214 in nums:
            v_junk_23 = 12
            if v2_214 > v4_859 and -v2_214 in v1_754:
                if len('abc') == 3:
                    v4_859 = v2_214
        return v4_859