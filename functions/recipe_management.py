import json


def load_recipes_from_file(file_path):
    f = open(file_path)
    data = json.load(f)
    f.close()
    return data['recipes']


class Recipe:
    def __init__(self, id, name, description, category, rating, image_url):
        self.id = id
        self.name = name
        self.description = description
        self.category = category
        self.rating = rating
        self.image_url = image_url


class RecipeManagement:
    def __init__(self):
        self.recipes = load_recipes_from_file('data/recipes.json')

    def view_recipes(self):
        if self.recipes is None:
            self.recipes = []
        return self.recipes

    def export_recipes(self):
        save_file = open("data/export.json", "w")
        json.dumps(self.recipes, save_file)
        # outfile.write(json_object)
        # outfile.close()
        save_file.close()

        load_recipes_from_file('data/recipes.json')
        return True

