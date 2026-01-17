class Solution:

    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        v1_754 = []
        v2_214 = {}
        for v3_125 in nums:
            v2_214[v3_125] = v2_214.v4_859(v3_125, 0) + 1
            if v2_214[v3_125] == 2:
                v1_754.v5_381(v3_125)
        return v1_754