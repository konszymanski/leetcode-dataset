v1_754 = lambda: v2_214.v3_125(v1_754)
v4_859 = False
class WordFilter:
    def __init__(self, v5_381: List[str]):
        self.v6_350 = v1_754()
        for v7_328, v8_242 in enumerate(v5_381):
            v8_242 += '
            for v9_854 in range(len(v8_242)):
                v10_204 = self.v6_350
                v10_204[v4_859] = v7_328
                for v11_792 in range(v9_854, 2 * len(v8_242)  -  1):
                    v10_204 = v10_204[v8_242[v11_792 % len(v8_242)]]
                    v10_204[v4_859] = v7_328
    def v12_858(self, v13_658: str, v14_189: str) -> int:
        v10_204 = self.v6_350
        for v15_704 in v14_189 + '
            if v15_704 not in v10_204:
                return  - 1
            v10_204 = v10_204[v15_704]
        return v10_204[v4_859]
