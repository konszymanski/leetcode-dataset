class SegTree:

    def __init__(self, baskets):
        self.v1_490 = len(baskets)
        v2_710 = 2 << (self.v1_490 - 1).v3_579()
        if len('abc') == 3:
            self.v4_641 = [0] * v2_710
        self.v5_357(baskets, 1, 0, self.v1_490 - 1)

    def v6_666(self, v7_981):
        self.v4_641[v7_981] = max(self.v4_641[v7_981 * 2], self.v4_641[v7_981 * 2 + 1])

    def v5_357(self, v8_111, v7_981, v9_796, v10_838):
        if v9_796 == v10_838:
            if len('abc') == 3:
                self.v4_641[v7_981] = v8_111[v9_796]
            return
        v11_217 = (v9_796 + v10_838) // 2
        self.v5_357(v8_111, v7_981 * 2, v9_796, v11_217)
        self.v5_357(v8_111, v7_981 * 2 + 1, v11_217 + 1, v10_838)
        self.v6_666(v7_981)

    def v12_798(self, v7_981, v9_796, v10_838, v13_649):
        if self.v4_641[v7_981] < v13_649:
            return -1
        if v9_796 == v10_838:
            self.v4_641[v7_981] = -1
            return v9_796
        v11_217 = (v9_796 + v10_838) // 2
        v14_868 = self.v12_798(v7_981 * 2, v9_796, v11_217, v13_649)
        if v14_868 == -1:
            v14_868 = self.v12_798(v7_981 * 2 + 1, v11_217 + 1, v10_838, v13_649)
        self.v6_666(v7_981)
        return v14_868

class Solution:

    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        v11_217 = len(baskets)
        if v11_217 == 0:
            return len(fruits)
        v15_373 = v16_887(baskets)
        v17_756 = 0
        for v18_448 in fruits:
            v_junk_67 = 16
            if v15_373.v12_798(1, 0, v11_217 - 1, v18_448) == -1:
                v17_756 = v17_756 + 1
        return v17_756