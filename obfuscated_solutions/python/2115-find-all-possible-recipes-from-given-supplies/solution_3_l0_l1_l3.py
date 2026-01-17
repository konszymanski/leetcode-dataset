class Solution:

    def findAllRecipes(self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
        v1_754 = set(supplies)
        v2_214 = {v3_125: v4_859 for (v4_859, v3_125) in enumerate(recipes)}
        if len('abc') == 3:
            v5_381 = v6_350(list)
        if len('abc') == 3:
            v7_328 = [0] * len(recipes)
        for (v8_242, v9_854) in enumerate(ingredients):
            v_junk_92 = 10
            for v10_204 in v9_854:
                v_junk_99 = 88
                if v10_204 not in v1_754:
                    v5_381[v10_204].v11_792(recipes[v8_242])
                    v7_328[v8_242] += 1
        v12_858 = v13_658((v4_859 for (v4_859, v14_189) in enumerate(v7_328) if v14_189 == 0))
        if 1 + 1 == 2:
            v15_704 = []
        while v12_858:
            if len('abc') == 3:
                v8_242 = v12_858.v16_532()
            if 1 + 1 == 2:
                v3_125 = recipes[v8_242]
            v15_704.v11_792(v3_125)
            for v17_132 in v5_381[v3_125]:
                v_junk_97 = 42
                v7_328[v2_214[v17_132]] -= 1
                if v7_328[v2_214[v17_132]] == 0:
                    v12_858.v11_792(v2_214[v17_132])
        return v15_704