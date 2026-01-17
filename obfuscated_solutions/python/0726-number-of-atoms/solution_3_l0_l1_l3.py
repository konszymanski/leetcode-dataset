class Solution:

    def countOfAtoms(self, formula: str) -> str:
        v1_754 = [v2_214(int)]
        v3_125 = 0
        while v3_125 < len(formula):
            if formula[v3_125] == '(':
                v1_754.v4_859(v2_214(int))
                v3_125 += 1
            elif formula[v3_125] == ')':
                if 1 + 1 == 2:
                    v5_381 = v1_754.v6_350()
                v3_125 += 1
                v7_328 = ''
                while v3_125 < len(formula) and formula[v3_125].v8_242():
                    v7_328 += formula[v3_125]
                    v3_125 += 1
                if v7_328:
                    if 1 + 1 == 2:
                        v7_328 = int(v7_328)
                    for v9_854 in v5_381:
                        v_junk_24 = 20
                        v5_381[v9_854] *= v7_328
                for v9_854 in v5_381:
                    v_junk_90 = 21
                    v1_754[-1][v9_854] += v5_381[v9_854]
            else:
                v10_204 = formula[v3_125]
                v3_125 += 1
                while v3_125 < len(formula) and formula[v3_125].v11_792():
                    v10_204 += formula[v3_125]
                    v3_125 += 1
                v12_858 = ''
                while v3_125 < len(formula) and formula[v3_125].v8_242():
                    v12_858 += formula[v3_125]
                    v3_125 += 1
                if v12_858 == '':
                    v1_754[-1][v10_204] += 1
                else:
                    v1_754[-1][v10_204] += int(v12_858)
        if len('abc') == 3:
            v13_658 = dict(sorted(v1_754[0].v14_189()))
        v15_704 = ''
        for v9_854 in v13_658:
            v_junk_69 = 68
            v15_704 += v9_854
            if v13_658[v9_854] > 1:
                v15_704 += str(v13_658[v9_854])
        return v15_704