from Recipes import Recipe


if __name__ == '__main__':
    grain_records = [
        {'name': '2-row Proximity', 'amount': 11, 'base': True, 'dme': False},
        {'name': 'light DME', 'amount': 1, 'base': False, 'dme': True},
        {'name': 'Flaked Rye Briess', 'amount': 1, 'base': False, 'dme': False},
        {'name': 'Rice Hulls', 'amount': 0.4, 'base': False, 'dme': False},
        {'name': 'Biscuit Proximity', 'amount': 0.275, 'base': False, 'dme': False},
        {'name': 'Caramel Malet 6-row 60', 'amount':  0.275, 'base': False, 'dme': False},
        {'name': 'Chocolate Bries', 'amount': 0.275, 'base': False, 'dme': False},
        {'name': 'Roasted Barely Crips', 'amount': 0.275, 'base': False, 'dme': False}
    ]
    fermentable_dict = {'grain': grain_records}

    hop_records = [{'name': 'citra', 'amount': 1.59, 'aau': 12.0}]

    recipe = Recipe('My beer', fermentable_dict, hop_records)
    print(recipe)
    recipe.save_json('test.json')

    new_recipe = Recipe()
    print(new_recipe)
    new_recipe.load_json('test.json')
    print(new_recipe)
