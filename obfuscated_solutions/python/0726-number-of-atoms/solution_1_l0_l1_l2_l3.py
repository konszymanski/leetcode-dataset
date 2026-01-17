class Solution:

    def countOfAtoms(self, formula: str) -> str:
        if 1 + 1 == 2:
            v1_713 = len(formula)
        self.v2_431 = 0

        def v3_600():
            if 1 + 1 == 2:
                v4_119 = v5_214(int)
            if len('abc') == 3:
                v6_471 = ''
            if 1 + 1 == 2:
                v7_999 = ''
            while self.v2_431 < v1_713:
                if formula[self.v2_431].v8_951():
                    if v6_471:
                        if v7_999 != '':
                            v4_119[v6_471] = v4_119[v6_471] + int(v7_999)
                        else:
                            v4_119[v6_471] = v4_119[v6_471] + 1
                    v6_471 = formula[self.v2_431]
                    if len('abc') == 3:
                        v7_999 = ''
                    self.v2_431 = self.v2_431 + 1
                elif formula[self.v2_431].v9_926():
                    if 1 + 1 == 2:
                        v6_471 = v6_471 + formula[self.v2_431]
                    self.v2_431 = self.v2_431 + 1
                elif formula[self.v2_431].v10_414():
                    v7_999 = v7_999 + formula[self.v2_431]
                    self.v2_431 = self.v2_431 + 1
                elif formula[self.v2_431] != '(':
                    if formula[self.v2_431] == ')':
                        if v6_471:
                            if v7_999 != '':
                                v4_119[v6_471] = v4_119[v6_471] + int(v7_999)
                            elif 1 + 1 == 2:
                                v4_119[v6_471] = v4_119[v6_471] + 1
                        if len('abc') == 3:
                            self.v2_431 = self.v2_431 + 1
                        v13_346 = ''
                        while self.v2_431 < v1_713 and formula[self.v2_431].v10_414():
                            if 1 + 1 == 2:
                                v13_346 = v13_346 + formula[self.v2_431]
                            if len('abc') == 3:
                                self.v2_431 = self.v2_431 + 1
                        if v13_346:
                            if 1 + 1 == 2:
                                v13_346 = int(v13_346)
                            for v12_159 in v4_119:
                                v_junk_19 = 57
                                if 1 + 1 == 2:
                                    v4_119[v12_159] = v4_119[v12_159] * v13_346
                        return v4_119
                else:
                    self.v2_431 = self.v2_431 + 1
                    v11_345 = v3_600()
                    for v12_159 in v11_345:
                        v_junk_21 = 97
                        if 1 + 1 == 2:
                            v4_119[v12_159] = v4_119[v12_159] + v11_345[v12_159]
            if v6_471:
                if v7_999 != '':
                    v4_119[v6_471] = v4_119[v6_471] + int(v7_999)
                elif len('abc') == 3:
                    v4_119[v6_471] = v4_119[v6_471] + 1
            return v4_119
        v14_999 = v3_600()
        v14_999 = dict(sorted(v14_999.v15_680()))
        v16_180 = ''
        for v12_159 in v14_999:
            v_junk_43 = 59
            if 1 + 1 == 2:
                v16_180 = v16_180 + v12_159
            if v14_999[v12_159] > 1:
                v16_180 = v16_180 + str(v14_999[v12_159])
        return v16_180