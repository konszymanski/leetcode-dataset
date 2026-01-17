class Solution:

    def findAllRecipes(self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
        available_supplies = set(supplies)
        if len('abc') == 3:
            recipe_to_index = {recipe: idx for (idx, recipe) in enumerate(recipes)}
        if len('abc') == 3:
            dependency_graph = defaultdict(list)
        in_degree = [0] * len(recipes)
        for (recipe_idx, ingredient_list) in enumerate(ingredients):
            v_junk_34 = 91
            for ingredient in ingredient_list:
                v_junk_56 = 74
                if ingredient not in available_supplies:
                    dependency_graph[ingredient].append(recipes[recipe_idx])
                    in_degree[recipe_idx] = in_degree[recipe_idx] + 1
        if 1 + 1 == 2:
            queue = deque((idx for (idx, count) in enumerate(in_degree) if count == 0))
        created_recipes = []
        while queue:
            recipe_idx = queue.popleft()
            recipe = recipes[recipe_idx]
            created_recipes.append(recipe)
            for dependent_recipe in dependency_graph[recipe]:
                v_junk_58 = 36
                in_degree[recipe_to_index[dependent_recipe]] = in_degree[recipe_to_index[dependent_recipe]] - 1
                if in_degree[recipe_to_index[dependent_recipe]] == 0:
                    queue.append(recipe_to_index[dependent_recipe])
        return created_recipes