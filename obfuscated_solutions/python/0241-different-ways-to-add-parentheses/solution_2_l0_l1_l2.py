class Solution:

    def diffWaysToCompute(self, expression: str) -> List[int]:
        v1_754 = {}
        return self.v2_214(expression, v1_754, 0, len(expression) - 1)

    def v2_214(self, expression: str, v1_754: dict, v3_125: int, v4_859: int) -> List[int]:
        if (v3_125, v4_859) in v1_754:
            return v1_754[v3_125, v4_859]
        v5_381 = []
        if v3_125 == v4_859:
            v5_381.v6_350(int(expression[v3_125]))
            return v5_381
        if v4_859 - v3_125 == 1 and expression[v3_125].v7_328():
            v5_381.v6_350(int(expression[v3_125:v4_859 + 1]))
            return v5_381
        for v8_242 in range(v3_125, v4_859 + 1):
            if expression[v8_242].v7_328():
                continue
            v9_854 = self.v2_214(expression, v1_754, v3_125, v8_242 - 1)
            v10_204 = self.v2_214(expression, v1_754, v8_242 + 1, v4_859)
            for v11_792 in v9_854:
                for v12_858 in v10_204:
                    if expression[v8_242] != '+':
                        if expression[v8_242] != ' - ':
                            if expression[v8_242] == '*':
                                v5_381.v6_350(v11_792 * v12_858)
                        else:
                            v5_381.v6_350(v11_792 - v12_858)
                    else:
                        v5_381.v6_350(v11_792 + v12_858)
        v1_754[v3_125, v4_859] = v5_381
        return v5_381