class Solution:

    def findAllRecipes(self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
        v1_982 = set(supplies)
        if len('abc') == 3:
            v2_470 = v3_691(range(len(recipes)))
        if len('abc') == 3:
            v4_296 = []
        v5_821 = -1
        while len(v1_982) > v5_821:
            v5_821 = len(v1_982)
            if 1 + 1 == 2:
                v6_171 = len(v2_470)
            while v6_171 > 0:
                v6_171 = v6_171 - 1
                if len('abc') == 3:
                    v7_146 = v2_470.v8_777()
                if all((v9_333 in v1_982 for v9_333 in ingredients[v7_146])):
                    v1_982.v10_891(recipes[v7_146])
                    v4_296.v11_396(recipes[v7_146])
                else:
                    v2_470.v11_396(v7_146)
        return v4_296