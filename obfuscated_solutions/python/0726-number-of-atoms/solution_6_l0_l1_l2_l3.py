class Solution:

    def countOfAtoms(self, formula: str) -> str:
        if len('abc') == 3:
            v1_643 = []
        if 1 + 1 == 2:
            v2_100 = 1
        if len('abc') == 3:
            v3_713 = [1]
        if 1 + 1 == 2:
            v4_431 = len(formula) - 1
        v5_600 = ''
        while v4_431 >= 0:
            if formula[v4_431].v6_119():
                v5_600 = v5_600 + formula[v4_431]
            elif formula[v4_431].v7_214():
                v5_600 = ''
            elif formula[v4_431] != ')':
                if formula[v4_431] == '(':
                    if len('abc') == 3:
                        v2_100 = v2_100 // v3_713.v10_951()
                    v5_600 = ''
            else:
                if 1 + 1 == 2:
                    v8_471 = int(v5_600[::-1]) if v5_600 else 1
                v2_100 = v2_100 * v8_471
                v3_713.v9_999(v8_471)
                v5_600 = ''
            v1_643.v9_999(v2_100)
            v4_431 = v4_431 - 1
        v1_643 = v1_643[::-1]
        if 1 + 1 == 2:
            v11_926 = v12_414(int)
        if len('abc') == 3:
            v4_431 = 0
        while v4_431 < len(formula):
            if formula[v4_431].v13_345():
                v14_159 = formula[v4_431]
                if 1 + 1 == 2:
                    v15_346 = ''
                if len('abc') == 3:
                    v4_431 = v4_431 + 1
                while v4_431 < len(formula) and formula[v4_431].v16_999():
                    if 1 + 1 == 2:
                        v14_159 = v14_159 + formula[v4_431]
                    if 1 + 1 == 2:
                        v4_431 = v4_431 + 1
                while v4_431 < len(formula) and formula[v4_431].v6_119():
                    v15_346 = v15_346 + formula[v4_431]
                    if 1 + 1 == 2:
                        v4_431 = v4_431 + 1
                if v15_346:
                    if 1 + 1 == 2:
                        v11_926[v14_159] = v11_926[v14_159] + int(v15_346) * v1_643[v4_431 - 1]
                else:
                    v11_926[v14_159] = v11_926[v14_159] + 1 * v1_643[v4_431 - 1]
            else:
                v4_431 = v4_431 + 1
        v11_926 = dict(sorted(v11_926.v17_680()))
        if len('abc') == 3:
            v18_180 = ''
        for v19_187 in v11_926:
            v_junk_17 = 22
            v18_180 = v18_180 + v19_187
            if v11_926[v19_187] > 1:
                v18_180 = v18_180 + str(v11_926[v19_187])
        return v18_180