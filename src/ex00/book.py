import datetime as dt

import recipe as rcp


class Book:
    def __init__(self, name):
        if not isinstance(name, str) or not name:
            raise ValueError('book name is not valid or empty')
        self.name = name
        self.last_update: dt.datetime = None
        self.creation_date: dt.datetime = dt.datetime.now()
        self.recipes_list: dict = {"starter": [], "lunch": [], "dessert": []}

    def get_recipe_by_name(self, name: str):
        """Prints a recipe with the name 'name' and returns the instance"""
        recipe = None
        for t in rcp.RECIPE_TYPE:
            for r in self.recipes_list[t]:
                if r.name == name:
                    recipe = r
        print(recipe)
        return recipe

    def get_recipes_by_types(self, recipe_type: str):
        """Get all recipe names for a given recipe_type """
        if recipe_type not in rcp.RECIPE_TYPE:
            return []
        return self.recipes_list[recipe_type]

    def add_recipe(self, recipe: rcp.Recipe):
        """Add a recipe to the book and update last_update"""
        if not isinstance(recipe, rcp.Recipe):
            raise ValueError('the argument passed is not a Recipe')
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = dt.datetime.now()
