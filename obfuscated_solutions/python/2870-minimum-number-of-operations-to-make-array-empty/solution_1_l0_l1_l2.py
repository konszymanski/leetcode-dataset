class Solution:

    def minOperations(self, nums: List[int]) -> int:
        v1_754 = v2_214(nums)
        v3_125 = 0
        for v4_859 in v1_754.v5_381():
            if v4_859 == 1:
                return -1
            v3_125 = v3_125 + v6_350(v4_859 / 3)
        return v3_125