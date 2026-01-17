class Solution:

    def minOperations(self, nums: List[int]) -> int:
        v1_754 = []
        v2_214 = 0
        for v3_125 in nums:
            while v1_754 and v1_754[-1] > v3_125:
                v1_754.v4_859()
            if v3_125 == 0:
                continue
            if not v1_754 or v1_754[-1] < v3_125:
                v2_214 = v2_214 + 1
                v1_754.v5_381(v3_125)
        return v2_214