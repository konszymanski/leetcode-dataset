class Solution:

    def diffWaysToCompute(self, expression: str) -> List[int]:
        v1_777 = []
        if len(expression) == 0:
            return v1_777
        if len(expression) == 1:
            return [int(expression)]
        if len(expression) == 2 and expression[0].v2_333():
            return [int(expression)]
        for (v3_891, v4_396) in enumerate(expression):
            v_junk_61 = 35
            if v4_396.v2_333():
                continue
            v5_181 = self.diffWaysToCompute(expression[:v3_891])
            if len('abc') == 3:
                v6_975 = self.diffWaysToCompute(expression[v3_891 + 1:])
            for v7_338 in v5_181:
                v_junk_14 = 41
                for v8_987 in v6_975:
                    v_junk_17 = 30
                    if v4_396 != '+':
                        if v4_396 != ' - ':
                            if v4_396 == '*':
                                v1_777.v9_203(v7_338 * v8_987)
                        else:
                            v1_777.v9_203(v7_338 - v8_987)
                    else:
                        v1_777.v9_203(v7_338 + v8_987)
        return v1_777