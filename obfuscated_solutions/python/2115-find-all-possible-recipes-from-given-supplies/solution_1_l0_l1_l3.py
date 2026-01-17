class Solution:

    def findAllRecipes(self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
        v1_754 = set(supplies)
        v2_214 = v3_125(range(len(recipes)))
        v4_859 = []
        v5_381 = -1
        while len(v1_754) > v5_381:
            v5_381 = len(v1_754)
            v6_350 = len(v2_214)
            while v6_350 > 0:
                v6_350 -= 1
                v7_328 = v2_214.v8_242()
                if all((v9_854 in v1_754 for v9_854 in ingredients[v7_328])):
                    v1_754.v10_204(recipes[v7_328])
                    v4_859.v11_792(recipes[v7_328])
                else:
                    v2_214.v11_792(v7_328)
        return v4_859