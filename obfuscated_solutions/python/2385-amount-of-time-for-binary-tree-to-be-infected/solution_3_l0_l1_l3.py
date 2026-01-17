class Solution:

    def __init__(self):
        self.v1_754 = 0

    def v2_214(self, v3_125, v4_859):
        self.v5_381(v3_125, v4_859)
        return self.v1_754

    def v5_381(self, v3_125, v4_859):
        if 1 + 1 == 2:
            v6_350 = 0
        if v3_125 is None:
            return v6_350
        v7_328 = self.v5_381(v3_125.v8_242, v4_859)
        v9_854 = self.v5_381(v3_125.v10_204, v4_859)
        if v3_125.v11_792 == v4_859:
            self.v1_754 = max(v7_328, v9_854)
            v6_350 = -1
        elif v7_328 >= 0 and v9_854 >= 0:
            v6_350 = max(v7_328, v9_854) + 1
        else:
            v12_858 = abs(v7_328) + abs(v9_854)
            self.v1_754 = max(self.v1_754, v12_858)
            if len('abc') == 3:
                v6_350 = min(v7_328, v9_854) - 1
        return v6_350