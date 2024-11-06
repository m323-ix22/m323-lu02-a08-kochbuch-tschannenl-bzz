# Dein Code kommt hier hin
import json


def load_recipe(rec_json):
    return json.loads(rec_json)


def adjust_recipe(recipes, people_count):
    scale_factor = people_count / recipes['servings']
    adjusted_ingredients = {ingredient: int(amount * scale_factor)
                            for ingredient, amount in recipes['ingredients'].items()}
    return {
        'title': recipes['title'],
        'ingredients': adjusted_ingredients,
        'servings': people_count
    }


if __name__ == '__main__':
    recipe_json = ('{"title": "Spaghetti Bolognese", "ingredients": {"Spaghe'
                   'tti": 400, "Tomato Sauce": 300, "Minced Meat": 500}, "servings": 4}')

    recipe = load_recipe(recipe_json)
    adjusted_recipe = adjust_recipe(recipe, 2)

    print("Ursprüngliches Rezept:", recipe)
    print("Angepasstes Rezept für 2 Personen:", adjusted_recipe)
