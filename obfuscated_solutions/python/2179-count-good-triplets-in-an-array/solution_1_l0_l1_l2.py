class FenwickTree:

    def __init__(self, v1_754):
        self.v2_214 = [0] * (v1_754 + 1)

    def v3_125(self, v4_859, v5_381):
        v4_859 = v4_859 + 1
        while v4_859 <= len(self.v2_214) - 1:
            self.v2_214[v4_859] = self.v2_214[v4_859] + v5_381
            v4_859 = v4_859 + (v4_859 & -v4_859)

    def v6_350(self, v4_859):
        v4_859 = v4_859 + 1
        v7_328 = 0
        while v4_859 > 0:
            v7_328 = v7_328 + self.v2_214[v4_859]
            v4_859 = v4_859 - (v4_859 & -v4_859)
        return v7_328

class Solution:

    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        v8_242 = len(nums1)
        (v9_854, v10_204) = ([0] * v8_242, [0] * v8_242)
        for (v11_792, v12_858) in enumerate(nums2):
            v9_854[v12_858] = v11_792
        for (v11_792, v13_658) in enumerate(nums1):
            v10_204[v9_854[v13_658]] = v11_792
        v2_214 = v14_189(v8_242)
        v7_328 = 0
        for v15_704 in range(v8_242):
            v16_532 = v10_204[v15_704]
            v17_132 = v2_214.v6_350(v16_532)
            v2_214.v3_125(v16_532, 1)
            v18_130 = v8_242 - 1 - v16_532 - (v15_704 - v17_132)
            v7_328 = v7_328 + v17_132 * v18_130
        return v7_328