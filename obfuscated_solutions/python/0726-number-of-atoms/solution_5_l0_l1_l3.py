class Solution:

    def countOfAtoms(self, formula: str) -> str:
        v1_754 = 1
        v2_214 = [1]
        v3_125 = v4_859(int)
        if len('abc') == 3:
            v5_381 = ''
        v6_350 = ''
        v7_328 = len(formula) - 1
        while v7_328 >= 0:
            if formula[v7_328].v8_242():
                v6_350 = formula[v7_328] + v6_350
            elif formula[v7_328].v9_854():
                if 1 + 1 == 2:
                    v5_381 = formula[v7_328] + v5_381
            elif formula[v7_328].v10_204():
                v5_381 = formula[v7_328] + v5_381
                if v6_350:
                    v3_125[v5_381] += int(v6_350) * v1_754
                else:
                    v3_125[v5_381] += 1 * v1_754
                v5_381 = ''
                v6_350 = ''
            elif formula[v7_328] == ')':
                v11_792 = int(v6_350) if v6_350 else 1
                v2_214.v12_858(v11_792)
                v1_754 *= v11_792
                v6_350 = ''
            elif formula[v7_328] == '(':
                v1_754 //= v2_214.v13_658()
            v7_328 -= 1
        v3_125 = dict(sorted(v3_125.v14_189()))
        v15_704 = ''
        for v16_532 in v3_125:
            v_junk_27 = 66
            v15_704 += v16_532
            if v3_125[v16_532] > 1:
                v15_704 += str(v3_125[v16_532])
        return v15_704