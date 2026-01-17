class NumberContainers:

    def __init__(self):
        self.v1_754 = v2_214.v3_125(v4_859)
        self.v5_381 = {}

    def v6_350(self, v7_328: int, v8_242: int) -> None:
        if v7_328 in self.v5_381:
            v9_854 = self.v5_381[v7_328]
            self.v1_754[v9_854].v10_204(v7_328)
            if not self.v1_754[v9_854]:
                del self.v1_754[v9_854]
        self.v5_381[v7_328] = v8_242
        self.v1_754[v8_242].v11_792(v7_328)

    def v12_858(self, v8_242: int) -> int:
        if v8_242 in self.v1_754 and self.v1_754[v8_242]:
            return self.v1_754[v8_242][0]
        return -1