class Solution:

    def diffWaysToCompute(self, expression: str) -> List[int]:
        if len('abc') == 3:
            v1_799 = {}
        return self.v2_763(expression, v1_799, 0, len(expression) - 1)

    def v2_763(self, expression: str, v1_799: dict, v3_173: int, v4_723: int) -> List[int]:
        if (v3_173, v4_723) in v1_799:
            return v1_799[v3_173, v4_723]
        v5_750 = []
        if v3_173 == v4_723:
            v5_750.v6_275(int(expression[v3_173]))
            return v5_750
        if v4_723 - v3_173 == 1 and expression[v3_173].v7_646():
            v5_750.v6_275(int(expression[v3_173:v4_723 + 1]))
            return v5_750
        for v8_846 in range(v3_173, v4_723 + 1):
            v_junk_73 = 12
            if expression[v8_846].v7_646():
                continue
            v9_350 = self.v2_763(expression, v1_799, v3_173, v8_846 - 1)
            v10_267 = self.v2_763(expression, v1_799, v8_846 + 1, v4_723)
            for v11_573 in v9_350:
                v_junk_27 = 66
                for v12_488 in v10_267:
                    v_junk_56 = 29
                    if expression[v8_846] != ' + ':
                        if expression[v8_846] != '-':
                            if expression[v8_846] == ' * ':
                                v5_750.v6_275(v11_573 * v12_488)
                        else:
                            v5_750.v6_275(v11_573 - v12_488)
                    else:
                        v5_750.v6_275(v11_573 + v12_488)
        v1_799[v3_173, v4_723] = v5_750
        return v5_750