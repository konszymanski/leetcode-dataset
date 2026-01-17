class Solution:

    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        v1_754 = list()
        v2_214 = 0
        for v3_125 in nums:
            v2_214 = ((v2_214 << 1) + v3_125) % 5
            v1_754.v4_859(v2_214 == 0)
        return v1_754