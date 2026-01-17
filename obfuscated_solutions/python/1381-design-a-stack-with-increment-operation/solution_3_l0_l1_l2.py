class CustomStack:

    def __init__(self, v1_754: int):
        self.v2_214 = [0] * v1_754
        self.v3_125 = [0] * v1_754
        self.v4_859 = -1

    def v5_381(self, v6_350: int) -> None:
        if self.v4_859 < len(self.v2_214) - 1:
            self.v4_859 = self.v4_859 + 1
            self.v2_214[self.v4_859] = v6_350

    def v7_328(self) -> int:
        if self.v4_859 < 0:
            return -1
        v8_242 = self.v2_214[self.v4_859] + self.v3_125[self.v4_859]
        if self.v4_859 > 0:
            self.v3_125[self.v4_859 - 1] = self.v3_125[self.v4_859 - 1] + self.v3_125[self.v4_859]
        self.v3_125[self.v4_859] = 0
        self.v4_859 = self.v4_859 - 1
        return v8_242

    def v9_854(self, v10_204: int, v11_792: int) -> None:
        if self.v4_859 >= 0:
            v12_858 = min(self.v4_859, v10_204 - 1)
            self.v3_125[v12_858] = self.v3_125[v12_858] + v11_792