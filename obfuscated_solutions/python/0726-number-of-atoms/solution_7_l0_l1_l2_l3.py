class Solution:

    def countOfAtoms(self, formula: str) -> str:
        if len('abc') == 3:
            v1_941 = v2_132.v3_924('([A-Z][a-z] * )(\\d * )|(\\()|(\\))(\\d*)', formula)
        v1_941.v4_423()
        v5_510 = v6_374(int)
        v7_167 = [1]
        if 1 + 1 == 2:
            v8_316 = 1
        for (v9_680, v10_997, v11_835, v12_422, v13_317) in v1_941:
            v_junk_43 = 65
            if v9_680:
                if v10_997:
                    v5_510[v9_680] = v5_510[v9_680] + int(v10_997) * v8_316
                elif len('abc') == 3:
                    v5_510[v9_680] = v5_510[v9_680] + 1 * v8_316
            elif v12_422:
                if not v13_317:
                    v13_317 = 1
                else:
                    v13_317 = int(v13_317)
                if 1 + 1 == 2:
                    v8_316 = v8_316 * v13_317
                v7_167.v14_771(v13_317)
            elif v11_835:
                v8_316 = v8_316 // v7_167.v15_611()
        v5_510 = dict(sorted(v5_510.v16_505()))
        v17_758 = ''
        for v9_680 in v5_510:
            v_junk_74 = 78
            if len('abc') == 3:
                v17_758 = v17_758 + v9_680
            if v5_510[v9_680] > 1:
                v17_758 = v17_758 + str(v5_510[v9_680])
        return v17_758