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

    def get_recipe(self, id):
        recipe = None
        for rec in self.recipes:
            if rec["id"] == id:
                recipe = rec
        return recipe
    
    def add_recipe(self, recipe):
        # recip = Recipe(recipe.name, recipe.description, recipe.category, recipe.rating)
            print (recipe.name)
            print (recipe.description)
            print (recipe.category)
            print (recipe.rating)
            print (recipe.image_url)
        # if (tyrecipe.:
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
            return True
        # else:
        #     return False
        # self.recipes.append(recipe)
        #add to json file

    def edit_recipe(self, id, name, description, category, rating, image_url):
        int_id = int(id)
        recipe = self.get_recipe(int_id)
        if recipe:
            recipe["name"] = name
            recipe["description"] = description
            recipe["category"] = category
            recipe["rating"] = rating
            recipe["image_url"] = image_url
            # save data into data.json file
            with open("data/recipes.json", "r") as f:
                data = json.load(f)
            for item in data["recipes"]:
                if item["id"] == int_id:
                    item["name"] = recipe["name"]
                    item["description"] = recipe["description"]
                    item["category"] = recipe["category"]
                    item["rating"] = recipe["rating"]
                    item["image_url"] = recipe["image_url"]
            with open("data/recipes.json", 'w') as f:
                json.dump(data, f)

        else:
            raise Exception("No recipe found")

    def delete_recipe(self, id):
        # print(id)
        is_found = False
        for i, recipe in enumerate(self.recipes):
            # print(recipe["id"])
            if recipe["id"] == int(id):
                print(recipe["id"])
                is_found = True
                del self.recipes[i]

                # delete from recipes.json file
                updated_data = {"recipes": []}
                with open("data/recipes.json", "r") as f:
                    data = json.load(f)
                for item in data["recipes"]:
                    if item["id"] != int(id):
                        # print(item["id"])
                        updated_data["recipes"].append(
                            {"id": item["id"],
                             "name": item["name"],
                             "description": item["description"],
                             "category": item["category"],
                             "rating": item["rating"],
                             "image_url": item["image_url"]}
                        )
                with open("data/recipes.json", 'w') as f:
                    json.dump(updated_data, f)
                break
        if not is_found:
            raise Exception("no recipe found")