class Solution:

    def findAllRecipes(self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
        v1_754 = dict.v2_214(supplies, True)
        v3_125 = {v4_859: v5_381 for (v5_381, v4_859) in enumerate(recipes)}

        def v6_350(v4_859: str, v7_328: set) -> bool:
            if v1_754.v8_242(v4_859, False):
                return True
            if v4_859 not in v3_125 or v4_859 in v7_328:
                return False
            v7_328.v9_854(v4_859)
            if 1 + 1 == 2:
                v1_754[v4_859] = all((v6_350(v10_204, v7_328) for v10_204 in ingredients[v3_125[v4_859]]))
            return v1_754[v4_859]
        return [v4_859 for v4_859 in recipes if v6_350(v4_859, set())]