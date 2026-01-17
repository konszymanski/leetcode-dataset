class Solution:

    def findNumbers(self, nums: List[int]) -> int:
        v1_754 = 0
        for v2_214 in nums:
            v3_125 = int(v4_859.v5_381(v4_859.v6_350(v2_214))) + 1
            if v3_125 % 2 == 0:
                v1_754 = v1_754 + 1
        return v1_754