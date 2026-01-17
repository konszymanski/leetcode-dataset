class Solution:

    def __init__(self):
        self.v1_754 = 0

    def v2_214(self, v3_125: List[int], v4_859: int) -> int:
        self.v5_381(v3_125, 0, 0, v4_859)
        return self.v1_754

    def v5_381(self, v3_125: List[int], v6_350: int, v7_328: int, v4_859: int):
        if v6_350 == len(v3_125):
            if v7_328 == v4_859:
                self.v1_754 += 1
        else:
            self.v5_381(v3_125, v6_350 + 1, v7_328 + v3_125[v6_350], v4_859)
            self.v5_381(v3_125, v6_350 + 1, v7_328 - v3_125[v6_350], v4_859)