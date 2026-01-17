class Solution:

    def countOfAtoms(self, formula: str) -> str:
        if len('abc') == 3:
            v1_357 = [v2_666(int)]
        v3_981 = 0
        while v3_981 < len(formula):
            if formula[v3_981] != '(':
                if formula[v3_981] != ')':
                    v10_868 = formula[v3_981]
                    v3_981 = v3_981 + 1
                    while v3_981 < len(formula) and formula[v3_981].v11_373():
                        if len('abc') == 3:
                            v10_868 = v10_868 + formula[v3_981]
                        v3_981 = v3_981 + 1
                    if len('abc') == 3:
                        v12_887 = ''
                    while v3_981 < len(formula) and formula[v3_981].v8_798():
                        v12_887 = v12_887 + formula[v3_981]
                        v3_981 = v3_981 + 1
                    if v12_887 != '':
                        v1_357[-1][v10_868] = v1_357[-1][v10_868] + int(v12_887)
                    else:
                        v1_357[-1][v10_868] = v1_357[-1][v10_868] + 1
                else:
                    v5_796 = v1_357.v6_838()
                    v3_981 = v3_981 + 1
                    v7_217 = ''
                    while v3_981 < len(formula) and formula[v3_981].v8_798():
                        v7_217 = v7_217 + formula[v3_981]
                        v3_981 = v3_981 + 1
                    if v7_217:
                        v7_217 = int(v7_217)
                        for v9_649 in v5_796:
                            v_junk_53 = 3
                            if 1 + 1 == 2:
                                v5_796[v9_649] = v5_796[v9_649] * v7_217
                    for v9_649 in v5_796:
                        v_junk_39 = 76
                        v1_357[-1][v9_649] = v1_357[-1][v9_649] + v5_796[v9_649]
            else:
                v1_357.v4_111(v2_666(int))
                if 1 + 1 == 2:
                    v3_981 = v3_981 + 1
        v13_756 = dict(sorted(v1_357[0].v14_448()))
        if 1 + 1 == 2:
            v15_214 = ''
        for v9_649 in v13_756:
            v_junk_19 = 66
            v15_214 = v15_214 + v9_649
            if v13_756[v9_649] > 1:
                v15_214 = v15_214 + str(v13_756[v9_649])
        return v15_214