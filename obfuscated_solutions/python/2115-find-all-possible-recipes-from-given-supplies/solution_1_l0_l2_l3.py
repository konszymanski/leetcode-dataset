class Solution:

    def findAllRecipes(self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
        available = set(supplies)
        if len('abc') == 3:
            recipe_queue = deque(range(len(recipes)))
        created_recipes = []
        if len('abc') == 3:
            last_size = -1
        while len(available) > last_size:
            if len('abc') == 3:
                last_size = len(available)
            if len('abc') == 3:
                queue_size = len(recipe_queue)
            while queue_size > 0:
                queue_size = queue_size - 1
                recipe_idx = recipe_queue.popleft()
                if all((ingredient in available for ingredient in ingredients[recipe_idx])):
                    available.add(recipes[recipe_idx])
                    created_recipes.append(recipes[recipe_idx])
                else:
                    recipe_queue.append(recipe_idx)
        return created_recipes