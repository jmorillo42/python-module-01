from book import Book
from recipe import Recipe


def testing_recipe_init(args):
    print(f'- Recipe {args} --> ', end='')
    try:
        Recipe(*args)
        print('FAIL')
    except ValueError as ex:
        print(f'OK ({ex})')


print('Testing Recipe:')
print()

testing_recipe_init((1, 1, 1, ['ajo'], '', 'lunch'))
testing_recipe_init(('', 1, 1, ['ajo'], '', 'lunch'))
testing_recipe_init((['error'], 1, 1, ['ajo'], '', 'lunch'))
testing_recipe_init((['error'], 1, 1, ['ajo'], '', 'lunch'))

testing_recipe_init(('ajo', 0, 1, ['ajo'], '', 'lunch'))
testing_recipe_init(('ajo', 6, 1, ['ajo'], '', 'lunch'))
testing_recipe_init(('ajo', 'error', 1, ['ajo'], '', 'lunch'))

testing_recipe_init(('ajo', 1, 0, ['ajo'], '', 'lunch'))
testing_recipe_init(('ajo', 1, 'error', ['ajo'], '', 'lunch'))
testing_recipe_init(('ajo', 1, -1, ['ajo'], '', 'lunch'))

testing_recipe_init(('ajo', 1, 1, [], '', 'lunch'))
testing_recipe_init(('ajo', 1, 1, None, '', 'lunch'))
testing_recipe_init(('ajo', 1, 1, 5, '', 'lunch'))
testing_recipe_init(('ajo', 1, 1, 'error', '', 'lunch'))
testing_recipe_init(('ajo', 1, 1, ['error', 42], '', 'lunch'))

testing_recipe_init(('ajo', 1, 1, ['ajo'], 5, 'lunch'))
testing_recipe_init(('ajo', 1, 1, ['ajo'], 1.5, 'lunch'))
testing_recipe_init(('ajo', 1, 1, ['ajo'], ['error'], 'lunch'))

testing_recipe_init(('ajo', 1, 1, ['ajo'], '', 'lunch '))
testing_recipe_init(('ajo', 1, 1, ['ajo'], '', ''))
testing_recipe_init(('ajo', 1, 1, ['ajo'], '', 5))
testing_recipe_init(('ajo', 1, 1, ['ajo'], '', ['lunch']))

print()

values = ('Sandwich', 1, 5, ['bread', 'ham', 'cheese'], 'Food consisting of sliced cheese and ham, placed between slices of bread', 'lunch')
print(f'Values: {values}')
print()
r = Recipe(*values)
print(r)

print()

print('Testing Book:')
print()

b = Book('CookBook')
print(f'''* Book: {b.name}
  Created: {b.creation_date}
  Updated: {b.last_update}
  Number of recipes: {sum([len(i) for i in b.recipes_list])}
''')

print('* Added Sandwich recipe to book')
b.add_recipe(r)
print(f'  {b.name} updated: {b.last_update}')

print()

print('* Get "Sandwich" recipe from book')
b.get_recipe_by_name('Sandwich')

print()

print('* Get "Cake" recipe from book')
b.get_recipe_by_name("Cake")

print()

print('* Get first lunch recipe from book')
print(b.get_recipes_by_types("lunch")[0])
# Should print the Crumble recipe

print()

print('* Get the recipes of type "foobar"')
print(b.get_recipes_by_types('foobar'))
# The recipe type does not exist, error must be handled in a justifiable manner
# such as returning None, [], or printing an error message
