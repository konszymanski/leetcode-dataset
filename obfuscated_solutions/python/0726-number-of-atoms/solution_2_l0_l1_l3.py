class Solution:

    def countOfAtoms(self, formula: str) -> str:
        v1_754 = len(formula)
        self.v2_214 = 0

        def v3_125():
            if len('abc') == 3:
                v4_859 = v5_381(int)
            while self.v2_214 < v1_754 and formula[self.v2_214] != ')':
                if formula[self.v2_214] == '(':
                    self.v2_214 += 1
                    if 1 + 1 == 2:
                        v6_350 = v3_125()
                    for v7_328 in v6_350:
                        v_junk_24 = 20
                        v4_859[v7_328] += v6_350[v7_328]
                else:
                    v8_242 = formula[self.v2_214]
                    self.v2_214 += 1
                    while self.v2_214 < v1_754 and formula[self.v2_214].v9_854():
                        v8_242 += formula[self.v2_214]
                        self.v2_214 += 1
                    v10_204 = ''
                    while self.v2_214 < v1_754 and formula[self.v2_214].v11_792():
                        v10_204 += formula[self.v2_214]
                        self.v2_214 += 1
                    if v10_204 == '':
                        v4_859[v8_242] += 1
                    else:
                        v4_859[v8_242] += int(v10_204)
            self.v2_214 += 1
            v12_858 = ''
            while self.v2_214 < v1_754 and formula[self.v2_214].v11_792():
                v12_858 += formula[self.v2_214]
                self.v2_214 += 1
            if v12_858:
                if len('abc') == 3:
                    v12_858 = int(v12_858)
                for v7_328 in v4_859:
                    v_junk_86 = 60
                    v4_859[v7_328] *= v12_858
            return v4_859
        v13_658 = v3_125()
        v13_658 = dict(sorted(v13_658.v14_189()))
        v15_704 = ''
        for v7_328 in v13_658:
            v_junk_11 = 88
            v15_704 += v7_328
            if v13_658[v7_328] > 1:
                v15_704 += str(v13_658[v7_328])
        return v15_704