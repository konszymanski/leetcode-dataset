class Solution:

    def subsets(self, nums):
        v1_754 = [[]]
        for v2_214 in nums:
            v3_125 = []
            for v4_859 in v1_754:
                v5_381 = v4_859.v6_350()
                v5_381.v7_328(v2_214)
                v3_125.v7_328(v5_381)
            for v4_859 in v3_125:
                v1_754.v7_328(v4_859)
        return v1_754