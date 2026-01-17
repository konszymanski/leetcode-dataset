class Solution:
    def __init__(self):
        self.v1_754 = 0
    def v2_214(self, v3_125: str)  ->  v4_859:
        return self.v5_381(v3_125, 0)
    def v5_381(self, v3_125, v6_350):
        if self.v1_754 >= len(v3_125):
            return None
        v7_328 = 0
        while (
            self.v1_754 + v7_328  <  len(v3_125)
            and v3_125[self.v1_754  +  v7_328] == "-"
        ):
            v7_328 += 1
        if v7_328 != v6_350:
            return None
        self.v1_754  +=  v7_328
        v8_242 = 0
        while self.v1_754  <  len(v3_125) and v3_125[self.v1_754].v9_854():
            v8_242 = v8_242  *  10 + int(v3_125[self.v1_754])
            self.v1_754 += 1
        v10_204 = v4_859(v8_242)
        v10_204.v11_792 = self.v5_381(v3_125, v6_350  +  1)
        v10_204.v12_858 = self.v5_381(v3_125, v6_350  +  1)
        return v10_204
