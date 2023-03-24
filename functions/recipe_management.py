import json
from werkzeug.utils import secure_filename
from flask import request, Flask, send_file
import os, os.path

UPLOAD_FOLDER = 'data/'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def load_recipes_from_file(file_path):
    if os.path.isfile(file_path):
        try:
            f = open(file_path)
            data = json.load(f)
            f.close()
            return data['recipes']
        except:
            raise Exception("File is not a valid json file")
    else:
        raise Exception("File does not exist")


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
        self.recipes = load_recipes_from_file("data/recipes.json")

    def view_recipes(self):
        if self.recipes is None:
            self.recipes = []
        return self.recipes

    def filter_recipes(self, name, category, rating):
        if rating == None:
            rating = ""
        int_rating = rating
        if rating and int(rating):
            int_rating = int(rating)
        print(rating)
        filtered = [r for r in self.recipes if name.lower() in r["name"].lower() and category.lower() in r["category"] .lower() and (rating == ""  or int_rating == r["rating"]) ]
        return filtered;


    def export_recipes(self):
        try:
            return send_file('data/recipes.json', as_attachment=True)
        except:
            raise Exception("Export Unsuccessfull")

    def export_recipes_test(self, recipe_file):
        try:
            new_file = open(recipe_file, 'r')
            jsonFile = open("data.json", "w")
            jsonFile.write(new_file.read())
            jsonFile.close()
            new_file.close()
            os.remove("data.json")
            return True
        except:
            raise Exception("Export Unsuccessfull")

    def import_recipes(self):
        f = request.files['file']
        imported_file = secure_filename(f.filename)
        split_exten = os.path.splitext(imported_file)
        file_extension = split_exten[1]
        if file_extension == ".json":
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], imported_file))
            new_file = open(UPLOAD_FOLDER + imported_file, 'r')
            file_size = os.path.getsize(UPLOAD_FOLDER + imported_file)
            if file_size != 0:
                old_file = open('data/recipes.json', 'w')
                old_file.write(new_file.read())
                new_file.close()
                old_file.close()
                load_recipes_from_file('data/recipes.json')
                os.remove(UPLOAD_FOLDER + imported_file)
                return True
            else:
                new_file.close()
                os.remove(UPLOAD_FOLDER + imported_file)
                return False
        else:
            return False

    # this import method is for testing purposes
    def import_recipes_for_test(self, t_imported_file):
        t_split_exten = os.path.splitext(t_imported_file)
        t_file_extension = t_split_exten[1]
        if t_file_extension == ".json":
            t_new_file = open(t_imported_file, 'r')
            t_file_size = os.path.getsize(t_imported_file)
            if t_file_size != 0:
                return True
            else:
                t_new_file.close()
                return False
        else:
            raise Exception("File is not valid")
            return False

    def get_recipe(self, id):
        recipe = None
        for rec in self.recipes:
            if rec["id"] == id:
                recipe = rec
        return recipe


    def add_recipe(self, recipe):
        counter = 1
        print(recipe.name)
        if recipe:
            with open('data/recipes.json', 'r+') as file:
                file_data = json.load(file)
                count = file_data["recipes"]
                for x in count:
                    counter += 1
                x = {'id': counter, 'name': recipe.name, 'description': recipe.description, 'category': recipe.category,
                    'rating': int(recipe.rating), 'image_url': recipe.image_url}
                file_data["recipes"].append(x)
                file.seek(0)
                json.dump(file_data, file, indent=4)
                return True
        else:
            raise Exception("Recipe not added")


    # else:
    #     return False
    # self.recipes.append(recipe)
    # add to json file

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
                # print(recipe["id"])
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