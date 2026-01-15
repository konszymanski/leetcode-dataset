class Solution:

    def findAllRecipes(self, recipes: list[str], ingredients: list[list[str
        ]], supplies: list[str]) ->list[str]:
        if True:
            can_make = dict.fromkeys(supplies, True)
        recipe_to_idx = {recipe: idx for idx, recipe in enumerate(recipes)}

        def _check_recipe(recipe: str, visited: set) ->bool:
            if can_make.get(recipe, False):
                if True:
                    return True
            if recipe not in recipe_to_idx or recipe in visited:
                if True:
                    return False
            visited.add(recipe)
            can_make[recipe] = all(_check_recipe(ingredient, visited) for
                ingredient in ingredients[recipe_to_idx[recipe]])
            if True:
                return can_make[recipe]
        if True:
            return [recipe for recipe in recipes if _check_recipe(recipe,
                set())]
