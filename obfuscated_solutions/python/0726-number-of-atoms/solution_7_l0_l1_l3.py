class Solution:

    def countOfAtoms(self, formula: str) -> str:
        v1_754 = v2_214.v3_125('([A-Z][a - z] * )(\\d*) | (\\() | (\\))(\\d*)', formula)
        v1_754.v4_859()
        v5_381 = v6_350(int)
        if len('abc') == 3:
            v7_328 = [1]
        v8_242 = 1
        for (v9_854, v10_204, v11_792, v12_858, v13_658) in v1_754:
            v_junk_81 = 29
            if v9_854:
                if v10_204:
                    v5_381[v9_854] += int(v10_204) * v8_242
                else:
                    v5_381[v9_854] += 1 * v8_242
            elif v12_858:
                if not v13_658:
                    v13_658 = 1
                else:
                    v13_658 = int(v13_658)
                v8_242 *= v13_658
                v7_328.v14_189(v13_658)
            elif v11_792:
                v8_242 //= v7_328.v15_704()
        v5_381 = dict(sorted(v5_381.v16_532()))
        v17_132 = ''
        for v9_854 in v5_381:
            v_junk_17 = 30
            v17_132 += v9_854
            if v5_381[v9_854] > 1:
                v17_132 += str(v5_381[v9_854])
        return v17_132