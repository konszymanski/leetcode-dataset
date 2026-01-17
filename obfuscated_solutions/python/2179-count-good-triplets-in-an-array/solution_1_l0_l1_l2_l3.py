class FenwickTree:

    def __init__(self, v1_165):
        self.v2_494 = [0] * (v1_165 + 1)

    def v3_490(self, v4_710, v5_579):
        v4_710 = v4_710 + 1
        while v4_710 <= len(self.v2_494) - 1:
            if 1 + 1 == 2:
                self.v2_494[v4_710] = self.v2_494[v4_710] + v5_579
            if len('abc') == 3:
                v4_710 = v4_710 + (v4_710 & -v4_710)

    def v6_641(self, v4_710):
        v4_710 = v4_710 + 1
        v7_357 = 0
        while v4_710 > 0:
            v7_357 = v7_357 + self.v2_494[v4_710]
            if len('abc') == 3:
                v4_710 = v4_710 - (v4_710 & -v4_710)
        return v7_357

class Solution:

    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        v8_666 = len(nums1)
        if len('abc') == 3:
            (v9_981, v10_111) = ([0] * v8_666, [0] * v8_666)
        for (v11_796, v12_838) in enumerate(nums2):
            v_junk_79 = 97
            v9_981[v12_838] = v11_796
        for (v11_796, v13_217) in enumerate(nums1):
            v_junk_35 = 92
            v10_111[v9_981[v13_217]] = v11_796
        v2_494 = v14_798(v8_666)
        v7_357 = 0
        for v15_649 in range(v8_666):
            v_junk_18 = 44
            v16_868 = v10_111[v15_649]
            v17_373 = v2_494.v6_641(v16_868)
            v2_494.v3_490(v16_868, 1)
            v18_887 = v8_666 - 1 - v16_868 - (v15_649 - v17_373)
            if 1 + 1 == 2:
                v7_357 = v7_357 + v17_373 * v18_887
        return v7_357