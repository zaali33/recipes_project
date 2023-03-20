import json
from werkzeug.utils import secure_filename
from flask import request, Flask
import os, os.path

UPLOAD_FOLDER = 'data/'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


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

    def import_recipes(self):
        f = request.files['file']
        imported_file = secure_filename(f.filename)
        split_exten = os.path.splitext(imported_file)
        file_extension = split_exten[1]
        # print("File Extension: ", file_extension)
        if file_extension == ".json":
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], imported_file))
            new_file = open(UPLOAD_FOLDER + imported_file, 'r')
            old_file = open('data/recipes.json', 'w')
            old_file.write(new_file.read())

            new_file.close()
            old_file.close()
            load_recipes_from_file('data/recipes.json')

            os.remove(UPLOAD_FOLDER + imported_file)
            return True
        else:
            return False

    def edit_recipe(self, recipe):
        recipe_from_file = None
        for rec in recipe_from_file:
            if rec.id == recipe.id:
                recipe_from_file = rec
                break
        if recipe_from_file is None:
            raiseExceptions("Recipe not found")
        recipe_from_file.id = recipe.id
        recipe_from_file.name = recipe.name
        recipe_from_file.description = recipe.description
        recipe_from_file.category = recipe.category
        recipe_from_file.rating = recipe.rating
        recipe_from_file.image_url = recipe.image_url

        return True    
    
    def add_recipe(self, recipe):
        # recip = Recipe(recipe.name, recipe.description, recipe.category, recipe.rating)
        counter = 1
        with open('data/recipes.json','r+') as file:
            file_data = json.load(file)
            count = file_data["recipes"]
            for x in count:
                counter += 1
            x = {'id':counter, 'name':recipe.name, 'description':recipe.description, 'category':recipe.category, 'rating':int(recipe.rating), 'image_url':recipe.image_url}
            file_data["recipes"].append(x)
            file.seek(0)
            json.dump(file_data, file, indent = 4)
        print(x)
        # self.recipes.append(recipe)
        #add to json file
