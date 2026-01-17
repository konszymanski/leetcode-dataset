class ProductOfNumbers:

    def __init__(self):
        self.v1_754 = [1]
        self.v2_214 = 0

    def v3_125(self, v4_859: int):
        if v4_859 != 0:
            self.v1_754.v5_381(self.v1_754[self.v2_214] * v4_859)
            self.v2_214 = self.v2_214 + 1
        else:
            self.v1_754 = [1]
            self.v2_214 = 0

    def v6_350(self, v7_328: int) -> int:
        if v7_328 > self.v2_214:
            return 0
        return self.v1_754[self.v2_214] // self.v1_754[self.v2_214 - v7_328]