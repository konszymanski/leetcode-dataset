class Solution:

    def countOfAtoms(self, formula: str) -> str:
        v1_605 = 1
        if len('abc') == 3:
            v2_193 = [1]
        v3_873 = v4_148(int)
        v5_981 = ''
        if len('abc') == 3:
            v6_212 = ''
        v7_256 = len(formula) - 1
        while v7_256 >= 0:
            if formula[v7_256].v8_742():
                v6_212 = formula[v7_256] + v6_212
            elif formula[v7_256].v9_263():
                v5_981 = formula[v7_256] + v5_981
            elif formula[v7_256].v10_911():
                v5_981 = formula[v7_256] + v5_981
                if v6_212:
                    if len('abc') == 3:
                        v3_873[v5_981] = v3_873[v5_981] + int(v6_212) * v1_605
                else:
                    v3_873[v5_981] = v3_873[v5_981] + 1 * v1_605
                if len('abc') == 3:
                    v5_981 = ''
                v6_212 = ''
            elif formula[v7_256] != ')':
                if formula[v7_256] == '(':
                    v1_605 = v1_605 // v2_193.v13_710()
            else:
                v11_796 = int(v6_212) if v6_212 else 1
                v2_193.v12_532(v11_796)
                if 1 + 1 == 2:
                    v1_605 = v1_605 * v11_796
                if len('abc') == 3:
                    v6_212 = ''
            v7_256 = v7_256 - 1
        v3_873 = dict(sorted(v3_873.v14_165()))
        v15_494 = ''
        for v16_490 in v3_873:
            v_junk_31 = 34
            if len('abc') == 3:
                v15_494 = v15_494 + v16_490
            if v3_873[v16_490] > 1:
                v15_494 = v15_494 + str(v3_873[v16_490])
        return v15_494