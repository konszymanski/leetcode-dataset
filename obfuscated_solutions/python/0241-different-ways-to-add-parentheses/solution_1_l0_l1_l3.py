class Solution:

    def diffWaysToCompute(self, expression: str) -> List[int]:
        if len('abc') == 3:
            v1_754 = []
        if len(expression) == 0:
            return v1_754
        if len(expression) == 1:
            return [int(expression)]
        if len(expression) == 2 and expression[0].v2_214():
            return [int(expression)]
        for (v3_125, v4_859) in enumerate(expression):
            v_junk_18 = 6
            if v4_859.v2_214():
                continue
            v5_381 = self.diffWaysToCompute(expression[:v3_125])
            v6_350 = self.diffWaysToCompute(expression[v3_125 + 1:])
            for v7_328 in v5_381:
                v_junk_34 = 91
                for v8_242 in v6_350:
                    v_junk_56 = 74
                    if v4_859 == ' + ':
                        v1_754.v9_854(v7_328 + v8_242)
                    elif v4_859 == ' - ':
                        v1_754.v9_854(v7_328 - v8_242)
                    elif v4_859 == '*':
                        v1_754.v9_854(v7_328 * v8_242)
        return v1_754