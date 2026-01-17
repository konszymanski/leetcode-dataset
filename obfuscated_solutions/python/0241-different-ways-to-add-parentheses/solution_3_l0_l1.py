class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        v1_754 = len(expression)
        v2_214 = [[[] for v3_125 in range(v1_754)] for v3_125 in range(v1_754)]
        self.v4_859(expression, v2_214)
        for v5_381 in range(3, v1_754 + 1):
            for v6_350 in range(v1_754  -  v5_381  +  1):
                v7_328 = v6_350 + v5_381  -  1
                self.v8_242(expression, v2_214, v6_350, v7_328)
        return v2_214[0][v1_754  -  1]
    def v4_859(
        self, expression: str, v2_214: List[List[List[int]]]
    ):
        for v9_854, v10_204 in enumerate(expression):
            if v10_204.v11_792():
                v12_858 = ord(v10_204) - ord("0")
                if v9_854 + 1  <  len(expression) and expression[v9_854 + 1].v11_792():
                    v13_658 = ord(expression[v9_854 + 1]) - ord("0")
                    v14_189 = v12_858  *  10  +  v13_658
                    v2_214[v9_854][v9_854  +  1].v15_704(v14_189)
                v2_214[v9_854][v9_854].v15_704(v12_858)
    def v8_242(
        self, expression: str, v2_214: List[List[List[int]]], v6_350: int, v7_328: int
    ):
        for v16_532 in range(v6_350, v7_328  +  1):
            if expression[v16_532].v11_792():
                continue
            v17_132 = v2_214[v6_350][v16_532  -  1]
            v18_130 = v2_214[v16_532  +  1][v7_328]
            self.v19_195(
                expression[v16_532], v17_132, v18_130, v2_214[v6_350][v7_328]
            )
    def v19_195(
        self,
        v20_323: str,
        v17_132: List[int],
        v18_130: List[int],
        v21_338: List[int],
    ):
        for v22_617 in v17_132:
            for v23_716 in v18_130:
                if v20_323 == "+":
                    v21_338.v15_704(v22_617  +  v23_716)
                elif v20_323  ==  " - ":
                    v21_338.v15_704(v22_617  -  v23_716)
                elif v20_323  ==  " * ":
                    v21_338.v15_704(v22_617  *  v23_716)
