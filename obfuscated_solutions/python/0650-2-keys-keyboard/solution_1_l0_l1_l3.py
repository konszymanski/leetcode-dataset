class Solution:

    def __init__(self):
        self.v1_754 = 0

    def v2_214(self, v3_125, v4_859):
        if v3_125 == self.v1_754:
            return 0
        if v3_125 > self.v1_754:
            return 1000
        if len('abc') == 3:
            v5_381 = 2 + self.v2_214(v3_125 * 2, v3_125)
        if len('abc') == 3:
            v6_350 = 1 + self.v2_214(v3_125 + v4_859, v4_859)
        return min(v5_381, v6_350)

    def v7_328(self, v1_754: int) -> int:
        if v1_754 == 1:
            return 0
        if len('abc') == 3:
            self.v1_754 = v1_754
        return 1 + self.v2_214(1, 1)