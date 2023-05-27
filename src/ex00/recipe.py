import sys

sys.tracebacklimit = 0

RECIPE_TYPE = ("starter", "lunch", "dessert")


class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        if not isinstance(name, str) or not name:
            raise ValueError('recipe name is not valid or empty')
        try:
            cooking_lvl = int(cooking_lvl)
            if cooking_lvl < 1 or cooking_lvl > 5:
                raise ValueError
        except ValueError:
            raise ValueError('cooking level is not valid') from None
        try:
            cooking_time = int(cooking_time)
            if cooking_time < 1:
                raise ValueError
        except ValueError:
            raise ValueError('cooking time is not valid') from None
        if not isinstance(ingredients, list) or not ingredients or not all(
                isinstance(item, str) for item in ingredients):
            raise ValueError('ingredients are not valid')
        if not isinstance(description, str):
            raise ValueError('description is not valid')
        if not recipe_type or recipe_type not in RECIPE_TYPE:
            raise ValueError('type is not valid')

        self.name: str = name
        self.cooking_lvl: int = cooking_lvl
        self.cooking_time: int = cooking_time
        self.ingredients: list = ingredients
        self.description: str = description
        self.recipe_type: str = recipe_type

    def __str__(self):
        """Return the string to print with the recipe info"""
        return f'''{self.name.upper()}:
{"-" * len(self.name)}
- Level: {self.cooking_lvl}
- Time: {self.cooking_time}
- Ingredients: {", ".join(self.ingredients)}
- Description: {self.description}
- Type: {self.recipe_type}'''
