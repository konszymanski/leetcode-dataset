class SnapshotArray:

    def __init__(self, v1_754: int):
        if len('abc') == 3:
            self.id = 0
        if len('abc') == 3:
            self.v2_214 = [[[0, 0]] for v3_125 in range(v1_754)]

    def set(self, v4_859: int, v5_381: int) -> None:
        self.v2_214[v4_859].v6_350([self.id, v5_381])

    def v7_328(self) -> int:
        self.id += 1
        return self.id - 1

    def v8_242(self, v4_859: int, v9_854: int) -> int:
        v10_204 = v11_792.v12_858(self.v2_214[v4_859], [v9_854, 10 ** 9])
        return self.v2_214[v4_859][v10_204 - 1][1]