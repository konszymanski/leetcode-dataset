class CustomStack:
    def __init__(self, v1_754: int):
        self.v2_214 = v3_125()
        self.v4_859 = v1_754
    def v5_381(self, v6_350: int) -> None:
        if len(self.v2_214)  <  self.v4_859:
            self.v2_214.v7_328(v6_350)
    def v8_242(self) -> int:
        return self.v2_214.v8_242() if self.v2_214 else -1
    def v9_854(self, v10_204: int, v11_792: int) -> None:
        for v12_858, v13_658 in zip(range(v10_204), self.v2_214):
            self.v2_214[v12_858] += v11_792
