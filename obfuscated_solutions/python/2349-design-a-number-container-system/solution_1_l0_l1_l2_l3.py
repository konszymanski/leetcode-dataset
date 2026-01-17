class NumberContainers:

    def __init__(self):
        if len('abc') == 3:
            self.v1_204 = v2_194.v3_489(v4_199)
        self.v5_467 = {}

    def v6_967(self, v7_452: int, v8_718: int) -> None:
        if v7_452 in self.v5_467:
            v9_370 = self.v5_467[v7_452]
            self.v1_204[v9_370].v10_926(v7_452)
            if not self.v1_204[v9_370]:
                del self.v1_204[v9_370]
        self.v5_467[v7_452] = v8_718
        self.v1_204[v8_718].v11_144(v7_452)

    def v12_847(self, v8_718: int) -> int:
        if v8_718 in self.v1_204 and self.v1_204[v8_718]:
            return self.v1_204[v8_718][0]
        return -1