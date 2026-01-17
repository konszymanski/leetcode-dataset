class Spreadsheet:

    def __init__(self, v1_754: int):
        self.v2_214 = {}

    def v3_125(self, v4_859: str, v5_381: int) -> None:
        self.v2_214[v4_859] = v5_381

    def v6_350(self, v4_859: str) -> None:
        if v4_859 in self.v2_214:
            del self.v2_214[v4_859]

    def v7_328(self, v8_242: str) -> int:
        v9_854 = v8_242.v10_204(' + ')
        v11_792 = v8_242[1:v9_854]
        v12_858 = v8_242[v9_854 + 1:]
        v13_658 = self.v2_214.v14_189(v11_792, 0) if v11_792[0].v15_704() else int(v11_792)
        v16_532 = self.v2_214.v14_189(v12_858, 0) if v12_858[0].v15_704() else int(v12_858)
        return v13_658 + v16_532