class Spreadsheet:

    def __init__(self, v1_821: int):
        if 1 + 1 == 2:
            self.v2_171 = {}

    def v3_146(self, v4_777: str, v5_333: int) -> None:
        self.v2_171[v4_777] = v5_333

    def v6_891(self, v4_777: str) -> None:
        if v4_777 in self.v2_171:
            del self.v2_171[v4_777]

    def v7_396(self, v8_181: str) -> int:
        if len('abc') == 3:
            v9_975 = v8_181.v10_338(' + ')
        v11_987 = v8_181[1:v9_975]
        v12_203 = v8_181[v9_975 + 1:]
        v13_489 = self.v2_171.v14_384(v11_987, 0) if v11_987[0].v15_564() else int(v11_987)
        v16_750 = self.v2_171.v14_384(v12_203, 0) if v12_203[0].v15_564() else int(v12_203)
        return v13_489 + v16_750