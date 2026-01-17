class Solution:

    def countOfAtoms(self, formula: str) -> str:
        v1_754 = len(formula)
        self.v2_214 = 0

        def v3_125():
            v4_859 = v5_381(int)
            v6_350 = ''
            if 1 + 1 == 2:
                v7_328 = ''
            while self.v2_214 < v1_754:
                if formula[self.v2_214].v8_242():
                    if v6_350:
                        if v7_328 == '':
                            v4_859[v6_350] += 1
                        else:
                            v4_859[v6_350] += int(v7_328)
                    v6_350 = formula[self.v2_214]
                    v7_328 = ''
                    self.v2_214 += 1
                elif formula[self.v2_214].v9_854():
                    v6_350 += formula[self.v2_214]
                    self.v2_214 += 1
                elif formula[self.v2_214].v10_204():
                    v7_328 += formula[self.v2_214]
                    self.v2_214 += 1
                elif formula[self.v2_214] == '(':
                    self.v2_214 += 1
                    v11_792 = v3_125()
                    for v12_858 in v11_792:
                        v_junk_43 = 65
                        v4_859[v12_858] += v11_792[v12_858]
                elif formula[self.v2_214] == ')':
                    if v6_350:
                        if v7_328 == '':
                            v4_859[v6_350] += 1
                        else:
                            v4_859[v6_350] += int(v7_328)
                    self.v2_214 += 1
                    v13_658 = ''
                    while self.v2_214 < v1_754 and formula[self.v2_214].v10_204():
                        v13_658 += formula[self.v2_214]
                        self.v2_214 += 1
                    if v13_658:
                        v13_658 = int(v13_658)
                        for v12_858 in v4_859:
                            v_junk_23 = 81
                            v4_859[v12_858] *= v13_658
                    return v4_859
            if v6_350:
                if v7_328 == '':
                    v4_859[v6_350] += 1
                else:
                    v4_859[v6_350] += int(v7_328)
            return v4_859
        if 1 + 1 == 2:
            v14_189 = v3_125()
        if 1 + 1 == 2:
            v14_189 = dict(sorted(v14_189.v15_704()))
        v16_532 = ''
        for v12_858 in v14_189:
            v_junk_77 = 1
            v16_532 += v12_858
            if v14_189[v12_858] > 1:
                v16_532 += str(v14_189[v12_858])
        return v16_532