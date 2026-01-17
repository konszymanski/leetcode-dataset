class Spreadsheet:

    def __init__(self, v1_754: int):
        self.v2_214 = [[0] * 27 for v3_125 in range(v1_754 + 1)]

    def v4_859(self, v5_381: str, v6_350: int) -> None:
        (v7_328, v8_242) = self.v9_854(v5_381)
        self.v2_214[v7_328][v8_242] = v6_350

    def v10_204(self, v5_381: str) -> None:
        (v7_328, v8_242) = self.v9_854(v5_381)
        self.v2_214[v7_328][v8_242] = 0

    def v11_792(self, v12_858: str) -> int:
        v13_658 = v12_858.v14_189(' + ')
        v15_704 = v12_858[1:v13_658]
        v16_532 = v12_858[v13_658 + 1:]
        return self.v17_132(v15_704) + self.v17_132(v16_532)

    def v9_854(self, v5_381):
        v7_328 = int(v5_381[1:])
        v8_242 = ord(v5_381[0]) - ord('A')
        return (v7_328, v8_242)

    def v17_132(self, v5_381):
        if v5_381[0].v18_130():
            (v7_328, v8_242) = self.v9_854(v5_381)
            return self.v2_214[v7_328][v8_242]
        else:
            return int(v5_381)