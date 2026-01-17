class KthLargest:
    def __init__(self, v1_754: int, v2_214: List[int]):
        self.v1_754 = v1_754
        self.v3_125 = v2_214
        self.v3_125.v4_859()
    def v5_381(self, v6_350: int) -> int:
        v7_328 = self.v8_242(v6_350)
        self.v3_125.v9_854(v7_328, v6_350)
        return self.v3_125[-self.v1_754]
    def v8_242(self, v6_350: int) -> int:
        v10_204, v11_792 = 0, len(self.v3_125) - 1
        while v10_204 <= v11_792:
            v12_858 = (v10_204  +  v11_792) // 2
            v13_658 = self.v3_125[v12_858]
            if v13_658  ==  v6_350:
                return v12_858
            elif v13_658  >  v6_350:
                v11_792 = v12_858 - 1
            else:
                v10_204 = v12_858  +  1
        return v10_204
