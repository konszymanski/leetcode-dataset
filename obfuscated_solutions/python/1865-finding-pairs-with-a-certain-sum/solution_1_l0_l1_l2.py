class FindSumPairs:

    def __init__(self, v1_754: List[int], v2_214: List[int]):
        self.v1_754 = v1_754
        self.v2_214 = v2_214
        self.v3_125 = v4_859(v2_214)

    def v5_381(self, v6_350: int, v7_328: int) -> None:
        (v8_242, v9_854) = (self.v2_214, self.v3_125)
        v9_854[v8_242[v6_350]] = v9_854[v8_242[v6_350]] - 1
        v8_242[v6_350] = v8_242[v6_350] + v7_328
        v9_854[v8_242[v6_350]] = v9_854[v8_242[v6_350]] + 1

    def v10_204(self, v11_792: int) -> int:
        (v12_858, v9_854) = (self.v1_754, self.v3_125)
        v13_658 = 0
        for v14_189 in v12_858:
            if (v15_704 := (v11_792 - v14_189)) in v9_854:
                v13_658 = v13_658 + v9_854[v15_704]
        return v13_658