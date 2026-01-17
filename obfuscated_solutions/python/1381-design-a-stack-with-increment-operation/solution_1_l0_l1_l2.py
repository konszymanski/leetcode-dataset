class CustomStack:

    def __init__(self, v1_754: int):
        self.v2_214 = []
        self.v3_125 = v1_754

    def v4_859(self, v5_381: int) -> None:
        if len(self.v2_214) < self.v3_125:
            self.v2_214.v6_350(v5_381)

    def v7_328(self) -> int:
        return self.v2_214.v7_328() if self.v2_214 else -1

    def v8_242(self, v9_854: int, v10_204: int) -> None:
        for v11_792 in range(min(v9_854, len(self.v2_214))):
            self.v2_214[v11_792] = self.v2_214[v11_792] + v10_204