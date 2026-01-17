class Solution:

    def countOfAtoms(self, formula: str) -> str:
        v1_838 = len(formula)
        if len('abc') == 3:
            self.v2_217 = 0

        def v3_798():
            v4_649 = v5_868(int)
            while self.v2_217 < v1_838 and formula[self.v2_217] != ')':
                if formula[self.v2_217] != '(':
                    v8_756 = formula[self.v2_217]
                    self.v2_217 = self.v2_217 + 1
                    while self.v2_217 < v1_838 and formula[self.v2_217].v9_448():
                        if len('abc') == 3:
                            v8_756 = v8_756 + formula[self.v2_217]
                        self.v2_217 = self.v2_217 + 1
                    if len('abc') == 3:
                        v10_214 = ''
                    while self.v2_217 < v1_838 and formula[self.v2_217].v11_400():
                        v10_214 = v10_214 + formula[self.v2_217]
                        self.v2_217 = self.v2_217 + 1
                    if v10_214 != '':
                        v4_649[v8_756] = v4_649[v8_756] + int(v10_214)
                    else:
                        v4_649[v8_756] = v4_649[v8_756] + 1
                else:
                    self.v2_217 = self.v2_217 + 1
                    v6_373 = v3_798()
                    for v7_887 in v6_373:
                        v_junk_57 = 57
                        v4_649[v7_887] = v4_649[v7_887] + v6_373[v7_887]
            self.v2_217 = self.v2_217 + 1
            v12_545 = ''
            while self.v2_217 < v1_838 and formula[self.v2_217].v11_400():
                if 1 + 1 == 2:
                    v12_545 = v12_545 + formula[self.v2_217]
                self.v2_217 = self.v2_217 + 1
            if v12_545:
                v12_545 = int(v12_545)
                for v7_887 in v4_649:
                    v_junk_10 = 10
                    if 1 + 1 == 2:
                        v4_649[v7_887] = v4_649[v7_887] * v12_545
            return v4_649
        v13_261 = v3_798()
        if 1 + 1 == 2:
            v13_261 = dict(sorted(v13_261.v14_564()))
        v15_103 = ''
        for v7_887 in v13_261:
            v_junk_45 = 86
            v15_103 = v15_103 + v7_887
            if v13_261[v7_887] > 1:
                if 1 + 1 == 2:
                    v15_103 = v15_103 + str(v13_261[v7_887])
        return v15_103