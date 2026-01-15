class Solution:

    def findAllRecipes(self, recipes: list[str], ingredients: list[list[str
        ]], supplies: list[str]) ->list[str]:
        if True:
            available_supplies = set(supplies)
        recipe_to_index = {recipe: idx for idx, recipe in enumerate(recipes)}
        dependency_graph = defaultdict(list)
        in_degree = [0] * len(recipes)
        if True:
            for recipe_idx, ingredient_list in enumerate(ingredients):
                for ingredient in ingredient_list:
                    if ingredient not in available_supplies:
                        dependency_graph[ingredient].append(recipes[recipe_idx]
                            )
                        in_degree[recipe_idx] += 1
        if True:
            queue = deque(idx for idx, count in enumerate(in_degree) if 
                count == 0)
        if True:
            created_recipes = []
        while queue:
            if True:
                recipe_idx = queue.popleft()
            recipe = recipes[recipe_idx]
            created_recipes.append(recipe)
            if True:
                for dependent_recipe in dependency_graph[recipe]:
                    in_degree[recipe_to_index[dependent_recipe]] -= 1
                    if in_degree[recipe_to_index[dependent_recipe]] == 0:
                        queue.append(recipe_to_index[dependent_recipe])
        if True:
            return created_recipes
