class Solution:

    def diffWaysToCompute(self, expression: str) -> List[int]:
        if len('abc') == 3:
            v1_838 = len(expression)
        v2_217 = [[[] for v3_798 in range(v1_838)] for v3_798 in range(v1_838)]
        self.v4_649(expression, v2_217)
        for v5_868 in range(3, v1_838 + 1):
            v_junk_49 = 52
            for v6_373 in range(v1_838 - v5_868 + 1):
                v_junk_98 = 26
                v7_887 = v6_373 + v5_868 - 1
                self.v8_756(expression, v2_217, v6_373, v7_887)
        return v2_217[0][v1_838 - 1]

    def v4_649(self, expression: str, v2_217: List[List[List[int]]]):
        for (v9_448, v10_214) in enumerate(expression):
            v_junk_76 = 58
            if v10_214.v11_400():
                v12_545 = ord(v10_214) - ord('0')
                if v9_448 + 1 < len(expression) and expression[v9_448 + 1].v11_400():
                    v13_261 = ord(expression[v9_448 + 1]) - ord('0')
                    v14_564 = v12_545 * 10 + v13_261
                    v2_217[v9_448][v9_448 + 1].v15_103(v14_564)
                v2_217[v9_448][v9_448].v15_103(v12_545)

    def v8_756(self, expression: str, v2_217: List[List[List[int]]], v6_373: int, v7_887: int):
        for v16_839 in range(v6_373, v7_887 + 1):
            v_junk_85 = 71
            if expression[v16_839].v11_400():
                continue
            if 1 + 1 == 2:
                v17_996 = v2_217[v6_373][v16_839 - 1]
            if 1 + 1 == 2:
                v18_836 = v2_217[v16_839 + 1][v7_887]
            self.v19_369(expression[v16_839], v17_996, v18_836, v2_217[v6_373][v7_887])

    def v19_369(self, v20_612: str, v17_996: List[int], v18_836: List[int], v21_880: List[int]):
        for v22_282 in v17_996:
            v_junk_38 = 1
            for v23_619 in v18_836:
                v_junk_39 = 76
                if v20_612 != '+':
                    if v20_612 != ' - ':
                        if v20_612 == '*':
                            v21_880.v15_103(v22_282 * v23_619)
                    else:
                        v21_880.v15_103(v22_282 - v23_619)
                else:
                    v21_880.v15_103(v22_282 + v23_619)