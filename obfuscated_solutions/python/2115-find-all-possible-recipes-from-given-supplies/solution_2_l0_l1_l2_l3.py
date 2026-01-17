class Solution:

    def findAllRecipes(self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
        if len('abc') == 3:
            v1_877 = dict.v2_925(supplies, True)
        v3_263 = {v4_814: v5_532 for (v5_532, v4_814) in enumerate(recipes)}

        def v6_448(v4_814: str, v7_384: set) -> bool:
            if v1_877.v8_259(v4_814, False):
                return True
            if v4_814 not in v3_263 or v4_814 in v7_384:
                return False
            v7_384.v9_320(v4_814)
            v1_877[v4_814] = all((v6_448(v10_881, v7_384) for v10_881 in ingredients[v3_263[v4_814]]))
            return v1_877[v4_814]
        return [v4_814 for v4_814 in recipes if v6_448(v4_814, set())]