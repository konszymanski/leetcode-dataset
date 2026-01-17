class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        v1_754 = -1
        v2_214 = set()
        for v3_125 in nums:
            v4_859 = abs(v3_125)
            if v4_859 > v1_754 and  - v3_125 in v2_214:
                v1_754 = v4_859
            v2_214.v5_381(v3_125)
        return v1_754
