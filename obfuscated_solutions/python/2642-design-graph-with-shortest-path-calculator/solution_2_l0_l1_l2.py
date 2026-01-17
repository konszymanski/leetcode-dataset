class Graph:

    def __init__(self, v1_754, v2_214):
        self.v3_125 = [[v4_859] * v1_754 for v5_381 in range(v1_754)]
        for (v6_350, v7_328, v8_242) in v2_214:
            self.v3_125[v6_350][v7_328] = v8_242
        for v9_854 in range(v1_754):
            self.v3_125[v9_854][v9_854] = 0
        for v9_854 in range(v1_754):
            for v10_204 in range(v1_754):
                for v11_792 in range(v1_754):
                    self.v3_125[v10_204][v11_792] = min(self.v3_125[v10_204][v11_792], self.v3_125[v10_204][v9_854] + self.v3_125[v9_854][v11_792])

    def v12_858(self, v13_658: List[int]) -> None:
        (v6_350, v7_328, v8_242) = v13_658
        v1_754 = len(self.v3_125)
        for v9_854 in range(v1_754):
            for v10_204 in range(v1_754):
                self.v3_125[v9_854][v10_204] = min(self.v3_125[v9_854][v10_204], self.v3_125[v9_854][v6_350] + self.v3_125[v7_328][v10_204] + v8_242)

    def v14_189(self, v15_704, v16_532):
        if self.v3_125[v15_704][v16_532] == v4_859:
            return -1
        return self.v3_125[v15_704][v16_532]