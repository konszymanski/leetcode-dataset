class Solution:
    def countOfAtoms(self, formula: str) -> str:
        v1_754 = []
        v2_214 = 1
        v3_125 = [1]
        v4_859 = len(formula)  -  1
        v5_381 = ""
        while v4_859  >=  0:
            if formula[v4_859].v6_350():
                v5_381 += formula[v4_859]
            elif formula[v4_859].v7_328():
                v5_381 = ""
            elif formula[v4_859] == ")":
                v8_242 = int(v5_381[:: - 1]) if v5_381 else 1
                v2_214  *=  v8_242
                v3_125.v9_854(v8_242)
                v5_381 = ""
            elif formula[v4_859]  ==  "(":
                v2_214 //= v3_125.v10_204()
                v5_381 = ""
            v1_754.v9_854(v2_214)
            v4_859  -=  1
        v1_754 = v1_754[:: - 1]
        v11_792 = v12_858(int)
        v4_859 = 0
        while v4_859  <  len(formula):
            if formula[v4_859].v13_658():
                v14_189 = formula[v4_859]
                v15_704 = ""
                v4_859  +=  1
                while v4_859  <  len(formula) and formula[v4_859].v16_532():
                    v14_189 += formula[v4_859]
                    v4_859  +=  1
                while v4_859  <  len(formula) and formula[v4_859].v6_350():
                    v15_704  +=  formula[v4_859]
                    v4_859 += 1
                if v15_704:
                    v11_792[v14_189] += int(v15_704) * v1_754[v4_859  -  1]
                else:
                    v11_792[v14_189]  +=  1  *  v1_754[v4_859  -  1]
            else:
                v4_859 += 1
        v11_792 = dict(sorted(v11_792.v17_132()))
        v18_130 = ""
        for v19_195 in v11_792:
            v18_130 += v19_195
            if v11_792[v19_195]  >  1:
                v18_130 += str(v11_792[v19_195])
        return v18_130
