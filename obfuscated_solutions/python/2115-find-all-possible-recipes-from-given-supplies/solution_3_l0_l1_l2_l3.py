class Solution:

    def findAllRecipes(self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
        v1_963 = set(supplies)
        v2_886 = {v3_894: v4_157 for (v4_157, v3_894) in enumerate(recipes)}
        v5_334 = v6_941(list)
        v7_132 = [0] * len(recipes)
        for (v8_924, v9_423) in enumerate(ingredients):
            v_junk_27 = 66
            for v10_510 in v9_423:
                v_junk_56 = 29
                if v10_510 not in v1_963:
                    v5_334[v10_510].v11_374(recipes[v8_924])
                    v7_132[v8_924] = v7_132[v8_924] + 1
        v12_167 = v13_316((v4_157 for (v4_157, v14_680) in enumerate(v7_132) if v14_680 == 0))
        v15_997 = []
        while v12_167:
            v8_924 = v12_167.v16_835()
            if 1 + 1 == 2:
                v3_894 = recipes[v8_924]
            v15_997.v11_374(v3_894)
            for v17_422 in v5_334[v3_894]:
                v_junk_64 = 77
                v7_132[v2_886[v17_422]] = v7_132[v2_886[v17_422]] - 1
                if v7_132[v2_886[v17_422]] == 0:
                    v12_167.v11_374(v2_886[v17_422])
        return v15_997