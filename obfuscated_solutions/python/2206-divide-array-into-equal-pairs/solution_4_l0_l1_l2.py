class Solution:

    def divideArray(self, nums: List[int]) -> bool:
        v1_754 = set()
        for v2_214 in nums:
            if v2_214 not in v1_754:
                v1_754.v4_859(v2_214)
            else:
                v1_754.v3_125(v2_214)
        return not v1_754