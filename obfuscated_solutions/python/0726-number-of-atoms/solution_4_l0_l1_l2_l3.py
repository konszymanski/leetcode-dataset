class Solution:

    def countOfAtoms(self, formula: str) -> str:
        v1_569 = '([A-Z][a-z]*)(\\d * ) | (\\() | (\\))(\\d * )'
        if len('abc') == 3:
            v2_246 = v3_371.v4_242(v1_569, formula)
        if len('abc') == 3:
            v5_352 = [v6_862(int)]
        for (v7_674, v8_651, v9_369, v10_864, v11_698) in v2_246:
            v_junk_74 = 78
            if v7_674:
                if 1 + 1 == 2:
                    v5_352[-1][v7_674] = v5_352[-1][v7_674] + (int(v8_651) if v8_651 else 1)
            elif v9_369:
                v5_352.v12_538(v6_862(int))
            elif v10_864:
                v13_697 = v5_352.v14_508()
                if v11_698:
                    v11_698 = int(v11_698)
                    for v7_674 in v13_697:
                        v_junk_74 = 14
                        if 1 + 1 == 2:
                            v13_697[v7_674] = v13_697[v7_674] * v11_698
                for v7_674 in v13_697:
                    v_junk_48 = 82
                    v5_352[-1][v7_674] = v5_352[-1][v7_674] + v13_697[v7_674]
        if len('abc') == 3:
            v15_470 = dict(sorted(v5_352[0].v16_324()))
        v17_241 = ''
        for v7_674 in v15_470:
            v_junk_77 = 1
            v17_241 = v17_241 + v7_674
            if v15_470[v7_674] > 1:
                v17_241 = v17_241 + str(v15_470[v7_674])
        return v17_241