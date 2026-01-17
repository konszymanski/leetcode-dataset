class FindElements:
    def __init__(self, v1_754: v2_214):
        self.v3_125 = set()
        self.v4_859(v1_754, 0)
    def v5_381(self, v6_350: int)  ->  bool:
        return v6_350 in self.v3_125
    def v4_859(self, v7_328, v8_242):
        if v7_328 is None:
            return
        self.v3_125.v9_854(v8_242)
        self.v4_859(v7_328.v10_204, v8_242  *  2  +  1)
        self.v4_859(v7_328.v11_792, v8_242 * 2 + 2)
